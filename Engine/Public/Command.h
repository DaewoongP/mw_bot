#pragma once
#include "Base.h"

BEGIN(Engine)

class CCommand abstract : public CBase
{
protected:
	explicit CCommand() = default;
	virtual ~CCommand() = default;

public:
	HRESULT CreateCommand(const string& strCommandName, const string& strCommandDescription, function<const dpp::slashcommand_t&> func);

public:
	virtual void Free() PURE;
};

END