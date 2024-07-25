#pragma once
#include "Command.h"

BEGIN(Engine)

class CCommandManager final : public CBase
{
	DECLARE_SINGLETON(CCommandManager)
private:
	explicit CCommandManager() = default;
	virtual ~CCommandManager() = default;

public:
	HRESULT Initialize();
	HRESULT AddCommand(const string& strCommandTag, CCommand* pCommand);
	//HRESULT DeleteCommand(const string& strCommandTag);

	HRESULT RegisterCommand();

private:
	_umap<const string&, CCommand*> m_Commands;

public:
	virtual void Free() override;
};

END