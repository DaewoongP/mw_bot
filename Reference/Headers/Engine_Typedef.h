#pragma once
namespace Engine
{
	typedef		signed char				_byte;
	typedef		char					_char;
	typedef		unsigned char			_ubyte;
	typedef		unsigned char			_uchar;

	typedef		wchar_t					_tchar;

	typedef		signed short			_short;
	typedef		unsigned short			_ushort;

	typedef		signed int				_int;
	typedef		unsigned int			_uint;

	typedef		signed long				_long;
	typedef		unsigned long			_ulong;

	typedef		int64_t					_tint;
	typedef		uint64_t				_tuint;
	
	typedef		float					_float;
	typedef		double					_double;

	typedef		bool					_bool;

	template<typename TypeKey, typename TypeValue>
	using		_umap					= std::unordered_map<TypeKey, TypeValue>;
}