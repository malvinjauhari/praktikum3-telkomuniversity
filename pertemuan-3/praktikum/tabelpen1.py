#Tabel penelusuran


#Logikanya
#Melakukan pengecekan jika <= 10, maka nilai total akan dikali 2, lalu akan menambah +1 ke n, selama perulangan berjalan
#Sehingga total yang didapatkan adalah  120

total = 0
n = 0

while n <= 10:
    total = total + n *2
    n = n + 1
print("Total =", total)

