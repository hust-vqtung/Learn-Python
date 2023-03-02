#include <iostream>
using namespace std;
double pow(double a, int b) {
    if(b==0) return 1;
    double res = 1;
    while(b!=0) {
        res *= a;
        b--;
    }
    return res;
}
int main(){
    int n, i=1;
    double x, sum = 0;
    cin >> n >> x;
    while (i<=n) {
        sum += pow(-1, i-1)*pow(x, i);
        i++;
    }
    cout << sum;
    return 0;
}