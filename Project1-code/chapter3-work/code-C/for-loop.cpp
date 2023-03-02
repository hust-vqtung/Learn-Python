#include <iostream>
using namespace std;
int main(){
    int n; cin >> n;
    int num[n+1];
    for (int i=2; i<=n; i++) {
        num[i] = 1;
    }
    for (int i=2; i<=n; i++) {
        for (int j=2; j<=n/i; j++) {
            num[i*j] = 0;
        }
    }
    for (int i=2; i<=n; i++) {
        if(num[i]==1) {
            cout << i << ' ';
        }
    }
    return 0;
}