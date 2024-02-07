#pragma once
namespace mw
{
	template <typename T>
	void Safe_Delete(T& pointer)
	{
		if (nullptr != pointer)
		{
			delete pointer;
			pointer = nullptr;
		}
	}

	template <typename T>
	void Safe_Delete_Array(T& pointer)
	{
		if (nullptr != pointer)
		{
			delete[] pointer;
			pointer = nullptr;
		}
	}

	class CTag_Finder
	{
	public:
		explicit CTag_Finder(const wchar_t* pTag)
			: m_pTargetTag(pTag)
		{
		}
		~CTag_Finder() = default;
	public:
		template<typename T>
		bool operator()(const T& pair)
		{
			if (0 == lstrcmpW(m_pTargetTag, pair.first))
			{
				return true;
			}

			return false;
		}

	private:
		const wchar_t* m_pTargetTag = nullptr;
	};
}