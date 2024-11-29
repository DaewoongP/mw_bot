#include "Bot.h"

IMPLEMENT_SINGLETON(CBot)

HRESULT CBot::Initialize(const string& strTokenPath)
{
	ifstream openFile(strTokenPath);
	if (!openFile.is_open())
	{
		MSG_BOX("Path is Invalid");
		return E_FAIL;
	}
	string strGuildID;

	getline(openFile, m_strToken);
	getline(openFile, strGuildID);
	openFile.close();

	stringstream ssInt(strGuildID);
	if (ssInt.fail())
	{
		MSG_BOX("Convert string to int failed");
		return E_FAIL;
	}
	ssInt >> m_iGuildID;

	if (false == isValid())
	{
		MSG_BOX("Invalid file data");
		return E_FAIL;
	}

	m_pCluster = new dpp::cluster(m_strToken);

	m_pCluster->on_log(dpp::utility::cout_logger());

	m_pCluster->on_slashcommand([&](const dpp::slashcommand_t& slashEvent) {
		if (slashEvent.command.get_command_name() == "ping") {

			slashEvent.reply(MW_TEXT("Å×¤Ñ½ºÆ® ±Â"));
		}
		});

	m_pCluster->on_ready([&](const dpp::ready_t& event) {
		if (dpp::run_once<struct register_bot_commands>()) {
			m_pCluster->global_command_create(
				dpp::slashcommand("ping", "Ping pong!", m_pCluster->me.id)
			);
		}
		});
	
	return S_OK;
}

HRESULT CBot::Apply()
{
	// st_wait -> normal mode
	// st_return -> check once (debug)
	m_pCluster->start(dpp::st_wait);

	m_pCluster->shutdown();

	return S_OK;
}

_bool CBot::isValid()
{
	if (-1 == m_iGuildID)
		return false;
	if ("" == m_strToken)
		return false;

	return true;
}

void CBot::Free()
{
	Safe_Delete(m_pCluster);
}
