#pragma once
#include "AppInstance.h"
#include "Client_Defines.h"

BEGIN(Client)

class CMainApp final : public CBase
{
private:
	explicit CMainApp();
	virtual ~CMainApp() = default;

public:
	HRESULT Initialize(const string& strTokenPath);

private:
	CAppInstance* m_pApp = nullptr;

public:
	static CMainApp* Create(const string& strTokenPath);
	virtual void Free() override;
};

END