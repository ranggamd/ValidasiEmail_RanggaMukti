import re

#bisa cek selain gmail.com, contoh : @yahoo.com dll
regex = '^[a-z0-9]+[/._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#Ketika kita hanya ingin cek khusus gmail.com saja
#regex = '^[a-z0-9]+[/._]?[a-z0-9]+[@]+[gmail]+[.]\w{2,3}$'

def cek(email):
    if (re.search(regex,email)):
        print("Email Valid")
    else:
        print("Email Tidak Valid")

if __name__ == "__main__":
    email = input("Masukan Email Address: ")
    cek(email)