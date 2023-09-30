#include "MainApp.h"

int main()
{
#ifdef _DEBUG
	_CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
#endif // _DEBUG

#ifdef _DEBUG
	cout << "Create Main App\n";
#endif // _DEBUG

	CMainApp* pMainApp = CMainApp::Create("../../Token.txt");



	Safe_Release(pMainApp);

	return 0;
}
