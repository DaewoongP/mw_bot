#include "..\Public\MainBot.h"

CMainBot::CMainBot()
	: m_szToken(""), m_iGuildID(-1)
{
}

HRESULT CMainBot::Initialize(const _char* pTokenPath)
{
	ifstream openFile(pTokenPath);
	if (!openFile.is_open())
	{
		cout << "Path is Invalid" << endl;
		return E_FAIL;
	}

	string szGuildID;

	getline(openFile, m_szToken);
	getline(openFile, szGuildID);
	openFile.close();

	stringstream ssInt(szGuildID);
	if (ssInt.fail())
	{
		cout << "Convert string to int failed" << endl;
		return E_FAIL;
	}
	ssInt >> m_iGuildID;

	if (false == isValid())
	{
		cout << "Invalid file data" << endl;
		return E_FAIL;
	}

	dpp::cluster bot(m_szToken);

	// 테스트용 -> 클래스로 변경.
	/* Output simple log messages to stdout */
	bot.on_log(dpp::utility::cout_logger());

	/* Handle slash command */
	bot.on_slashcommand([](const dpp::slashcommand_t& event) {
		if (event.command.get_command_name() == "ping") {
			event.reply("Pong!");
		}
		});

	/* Register slash command here in on_ready */
	bot.on_ready([&bot](const dpp::ready_t& event) {
		/* Wrap command registration in run_once to make sure it doesnt run on every full reconnection */
		if (dpp::run_once<struct register_bot_commands>()) {
			bot.global_command_create(dpp::slashcommand("ping", "Ping pong!", bot.me.id));
		}
		});

	bot.start(dpp::st_wait);

	return S_OK;
}

_bool CMainBot::isValid()
{
	if (-1 == m_iGuildID)
		return false;
	if ("" == m_szToken)
		return false;

	return true;
}

CMainBot* CMainBot::Create(const _char* pTokenPath)
{
	CMainBot* pInstance = new CMainBot;

	if (FAILED(pInstance->Initialize(pTokenPath)))
	{
		cout << "Failed Create MainApp" << endl;
		Safe_Delete(pInstance);
		return nullptr;
	}

	return pInstance;
}
