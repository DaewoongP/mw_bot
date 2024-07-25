#include "CommandManager.h"

IMPLEMENT_SINGLETON(CCommandManager)

HRESULT CCommandManager::Initialize()
{
    return S_OK;
}

HRESULT CCommandManager::AddCommand(const string& strCommandTag, CCommand* pCommand)
{
    return S_OK;
}

HRESULT CCommandManager::RegisterCommand()
{
    for (auto& pairCommand : m_Commands)
    {
        pairCommand.second->
    }

    return S_OK;
}

void CCommandManager::Free()
{
}
