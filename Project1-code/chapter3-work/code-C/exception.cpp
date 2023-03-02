#include <iostream>
using namespace std;

double division(float a, float b) {
    if(b == 0)
        throw "Division by zero!";
    return (a/b);
}
int main() {
    float x, y;
    cin >> x >> y;
    double z = 0;
 
    try {
        z = division(x, y);
        cout << z << endl;
    } catch (const char* msg) {
        cerr << msg << endl;
    }
    return 0;
}