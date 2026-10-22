TARGET = 50

HARI = 10


total = 0 #Akumulator
di_bawah = 0  #Pencacah

for hari in range (1, HARI + 1):
    produksi = int(input(f"Produksi hari ke- {hari} :"))
    total = total + produksi
    if produksi < TARGET :
        di_bawah = di_bawah + 1


print("Total produksi", total)
print("Rata rata per hari", total / HARI)
print("Hari dibawah target :", di_bawah)


#Terhitung
# Hari dibawah target 50 : 2 (total 40)

#Variabel Capslock : Karena menandakan konstanta dan tidak bisa dirubah nilainy
