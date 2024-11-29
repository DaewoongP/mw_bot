#pragma once
#include "Base.h"

BEGIN(Engine)

class CAppInstance final : public CBase
{
	DECLARE_SINGLETON(CAppInstance);
private:
	explicit CAppInstance();
	virtual ~CAppInstance() = default;

public:
	HRESULT Initialize(const string& strTokenPath);

private:
	class CBot* m_pBot = nullptr;
	class CCommandManager* m_pCommandManager = nullptr;

public:
	static void Shutdown();
	virtual void Free() override;
};

END