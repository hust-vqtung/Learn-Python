#include <iostream>
using namespace std;
int fb[100];
int memFibo(int n) {
	if(n<2) return n;
    else {
        if (fb[n] == 0) {
            fb[n] = memFibo(n-1) + memFibo(n-2);
        }
        return fb[n];
    }
}
int main() {
	int n; cin >> n;
	int i = 0;
    while (memFibo(i)<=n) {
        cout << memFibo(i) << ' ';
        i++;
    }
	return 0;
}