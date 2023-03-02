#include<iostream>
using namespace std;
int main(){
	string s; getline(cin, s);
    // remove space at beginning
    while(s[0]==' ')
        s = s.substr(1);
    // remove space at ending
    while(s[s.length()-1]==' ') 
        s.erase(s.end()-1);
    // remove multi space at middle
    int i = 0;
    while(i<s.length()) {
        if(s[i]==' ')
            while(s[i+1]==' ')
                s.erase(s.begin()+i+1);
        i++;
    }
    for(int i=0; i<s.length(); i++)
        s[i] = toupper(s[i]);
    cout << s;
	return 0;
}