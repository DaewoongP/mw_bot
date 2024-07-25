#pragma once
#include "Base.h"

BEGIN(Engine)

class CBot final : public CBase
{
	DECLARE_SINGLETON(CBot);
private:
	explicit CBot() = default;
	virtual ~CBot() = default;

public:
	string Get_Token() { return const_cast<string&>(static_cast<const CBot&>(*this).Get_Token()); }
	const string& Get_Token() const { return m_strToken; }

public:
	HRESULT Initialize(const string& strTokenPath);
	HRESULT Apply();

private:
	dpp::cluster*	m_pCluster = nullptr;
	string			m_strToken = "";
	_tint			m_iGuildID = -1;

private:
	_bool isValid();

public:
	virtual void Free() override;
};

END