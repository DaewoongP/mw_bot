#include "MainApp.h"

int main()
{
#ifdef _DEBUG
	cout << "Create Main App\n";
#endif // _DEBUG

    CMainApp* pMainApp = CMainApp::Create("../../Token.txt");

    Safe_Release(pMainApp);

	return 0;
}
