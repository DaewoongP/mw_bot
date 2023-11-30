#pragma once
#include "Includes.h"

BEGIN(mw)

class CMainBot
{
private:
	explicit CMainBot() = default;
	virtual ~CMainBot() = default;

public:
	HRESULT Initialize(const _char* pTokenPath);

private:
	string			m_szToken = "";
	_tint			m_iGuildID = { -1 };

private:
	_bool isValid();

public:
	static CMainApp* Create(const _char* pTokenPath);
};

END