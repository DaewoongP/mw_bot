#pragma once
#include "Base.h"
#include "Client_Defines.h"

BEGIN(Client)

class CMainApp final : public CBase
{
private:
	explicit CMainApp() = default;
	virtual ~CMainApp() = default;

public:
	HRESULT Initialize(const _char* pTokenPath);

private:
	string			m_szToken = "";
	_tint			m_iGuildID = { -1 };

private:
	_bool isValid();

public:
	static CMainApp* Create(const _char* pTokenPath);
	virtual void Free() override;
};

END