#pragma once
#define			ZEROMEM(_ptr)					ZeroMemory(_ptr, sizeof *_ptr)
#ifndef			MSG_BOX
#define			MSG_BOX(_message)				Error_Message_Box(_message)
#endif

#define			BEGIN(NAMESPACE)				namespace NAMESPACE {
#define			END								}



//singleton
#define NO_COPY(CLASSNAME)										\
		private:												\
		CLASSNAME(const CLASSNAME&) = delete;					\
		CLASSNAME& operator = (const CLASSNAME&) = delete;		

#define DECLARE_SINGLETON(CLASSNAME)							\
		NO_COPY(CLASSNAME)										\
		private:												\
		static CLASSNAME*	m_pInstance;						\
		public:													\
		static CLASSNAME*	GetInstance( void );				\
		static unsigned long DestroyInstance( void );			

#define IMPLEMENT_SINGLETON(CLASSNAME)							\
		CLASSNAME*	CLASSNAME::m_pInstance = nullptr;			\
		CLASSNAME*	CLASSNAME::GetInstance( void )	{			\
			if(nullptr == m_pInstance) {						\
				m_pInstance = New CLASSNAME;					\
			}													\
			return m_pInstance;									\
		}														\
		unsigned long CLASSNAME::DestroyInstance( void ) {		\
			unsigned long dwRefCnt = { 0 };						\
			if(nullptr != m_pInstance)							\
			{													\
				dwRefCnt = m_pInstance->Release();				\
				if(0 == dwRefCnt)								\
					m_pInstance = { nullptr };					\
			}													\
			return dwRefCnt;									\
		}