#include "AppInstance.h"
#include "Bot.h"
#include "CommandManager.h"

IMPLEMENT_SINGLETON(CAppInstance)

CAppInstance::CAppInstance()
	: m_pBot(CBot::GetInstance())
	, m_pCommandManager(CCommandManager::GetInstance())
{
	Safe_AddRef(m_pBot);
}

HRESULT CAppInstance::Initialize(const string& strTokenPath)
{
	FAILED_CHECK_RETURN(m_pBot->Initialize(strTokenPath), E_FAIL);

	m_pBot->Apply();

	return S_OK;
}

void CAppInstance::Shutdown()
{
	CBot::DestroyInstance();

	CCommandManager::DestroyInstance();

	CAppInstance::DestroyInstance();
}

void CAppInstance::Free()
{
	Safe_Release(m_pCommandManager);
	Safe_Release(m_pBot);
}
