#include "..\Public\MainApp.h"

CMainApp::CMainApp()
    : m_pApp(CAppInstance::GetInstance())
{
    Safe_AddRef(m_pApp);
}

HRESULT CMainApp::Initialize(const string& strTokenPath)
{
    m_pApp->Initialize(strTokenPath);

    return S_OK;
}

CMainApp* CMainApp::Create(const string& strTokenPath)
{
    CMainApp* pInstance = new CMainApp;

    if (FAILED(pInstance->Initialize(strTokenPath)))
    {
        MSG_BOX("Failed Create MainApp");
        Safe_Release(pInstance);
        return nullptr;
    }

    return pInstance;
}

void CMainApp::Free()
{
    Safe_Release(m_pApp);

    m_pApp->Shutdown();
}
