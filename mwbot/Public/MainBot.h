#pragma once
#include "Includes.h"

BEGIN(mw)

class CMainBot
{
public:
	explicit CMainBot();
	virtual ~CMainBot() = default;

public:
	HRESULT Initialize(const _char* pTokenPath);

private:
	string			m_szToken;
	_int			m_iGuildID;

private:
	_bool isValid();

public:
	static CMainBot* Create(const _char* pTokenPath);
};

END