#include<iostream>
#include<math.h>
using namespace std;
typedef struct {
    string ten;
    float x, y, z;
} toado;

int main() {
    toado t1, t2;
    cin >> t1.ten >> t1.x >> t1.y >> t1.z;
    cout << t1.ten << '(' << t1.x << ',' \
    << t1.y << ',' << t1.z << ")\n";
    cin >> t2.ten >> t2.x >> t2.y >> t2.z;
    cout << t2.ten << '(' << t2.x << ',' \
    << t2.y << ',' << t2.z << ")\n";
    cout << "Khoang cach: " << \
    sqrt((t1.x-t2.x)*(t1.x-t2.x) \
        + (t1.y-t2.y)*(t1.y-t2.y) \
        + (t1.z-t2.z)*(t1.z-t2.z));
    return 0;
}