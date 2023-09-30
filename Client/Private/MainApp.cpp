#include "..\Public\MainApp.h"

HRESULT CMainApp::Initialize(const _char* pTokenPath)
{
	ifstream openFile(pTokenPath);
	if (!openFile.is_open()) 
	{
		MSG_BOX("Path is Invalid");
		return E_FAIL;
	}
	string szGuildID;

	getline(openFile, m_szToken);
	getline(openFile, szGuildID);
	openFile.close();

	stringstream ssInt(szGuildID);
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

	dpp::cluster bot(m_szToken);

	bot.on_log(dpp::utility::cout_logger());

	bot.on_slashcommand([](const dpp::slashcommand_t& event) {
		if (event.command.get_command_name() == "ping") {
			event.reply("Pong!");
		}
	});

	bot.on_ready([&bot](const dpp::ready_t& event) {
		if (dpp::run_once<struct register_bot_commands>()) {
			bot.global_command_create(
				dpp::slashcommand("ping", "Ping pong!", bot.me.id)
			);
		}
	});

	bot.start(dpp::st_wait);
	
    return S_OK;
}

_bool CMainApp::isValid()
{
	if (-1 == m_iGuildID)
		return false;
	if ("" == m_szToken)
		return false;

	return true;
}

CMainApp* CMainApp::Create(const _char* pTokenPath)
{
    CMainApp* pInstance = new CMainApp;

    if (FAILED(pInstance->Initialize(pTokenPath)))
    {
        MSG_BOX("Failed Create MainApp");
		Safe_Release(pInstance);
        return nullptr;
    }

    return pInstance;
}

void CMainApp::Free()
{
}
