#looping kondisi batas
n = int(input("Jumlah 1 sampai n, n="))
total = 0

i = 1

while i <= n :
    total = total + i
    i = i +1

print("Jumlah : ", total)

#Misal input: 3
#total = 0 + 1 = 1, i = 2
#total = 1 + 2 = 3, i = 3
#total = 3 + 3 = 6, i = 4
#i=4 tidak memenuhi condition



