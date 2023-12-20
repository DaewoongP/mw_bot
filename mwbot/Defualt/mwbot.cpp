#pragma once
#include "MainBot.h"

int main()
{
	CMainBot* pBot = CMainBot::Create("../../Token.txt");

	Safe_Delete(pBot);

	return 0;
}