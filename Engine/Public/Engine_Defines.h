#pragma once
#pragma warning(disable : 4251)
#pragma warning(disable : 4819)

#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <array>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <functional>
#include <filesystem>

namespace fs = std::filesystem;

#include <dpp/dpp.h>

#include "Engine_Macros.h"
#include "Engine_Typedef.h"
#include "Engine_Functions.h"

#ifdef _DEBUG

#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

#ifndef DBG_NEW 

#define DBG_NEW new ( _NORMAL_BLOCK , __FILE__ , __LINE__ ) 
#define new DBG_NEW 

#endif // DBG_NEW
#endif // _DEBUG

using namespace std;
using namespace Engine;