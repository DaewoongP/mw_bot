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


// curl
#define CURL_STATICLIB
#include <curl/curl.h>

#pragma comment (lib, "wldap32.lib")
#pragma comment (lib, "ws2_32.lib")

// ~curl

using namespace std;
using namespace Engine;