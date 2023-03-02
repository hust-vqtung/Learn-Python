
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

listAccount = []

f = open("account.txt", "r")
rl = f.readlines()
for i in rl:
    s = i.split()
    listAccount.append(Account(s[0], s[1].strip()))
f.close()

for i in listAccount:
    print(i.username, i.password)