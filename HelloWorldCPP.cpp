#include <Windows.h>

using namespace std;

int main() {
	FreeConsole();

	MessageBox(NULL, "Hello World!", "C++", MB_OKCANCEL);

	return 0;
}