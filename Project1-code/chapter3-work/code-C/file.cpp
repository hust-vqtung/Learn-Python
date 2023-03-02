#include<iostream>
#include<string.h>
using namespace std;

struct Account {
	char username[100];
	char password[100];
};
Account listAccount[100];
void readAccount() {
	FILE *fptr = fopen("account.txt", "r");
	char buff[100];
	int i = 0, j = 0;
	while (fscanf(fptr, "%s", buff) == 1) {
		if (i % 2 == 0) {
			strcpy(listAccount[j].username, buff);
		}
		else {
			strcpy(listAccount[j].password, buff);
			j++;
		}
		i++;
	}
	fclose(fptr);
}

int main() {
    readAccount();
    int i = 0;
    while(strcmp(listAccount[i].username, "")) {
        cout << listAccount[i].username << ' ' \
        << listAccount[i].password << '\n';
        i++;
    }
}