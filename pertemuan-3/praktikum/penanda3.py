#Looping masukan penanda dan data kosong

total = 0
banyak = 0 

durasi = int(input("Waktu proses (menit, -1 selesai :)"))

while durasi != -1:
    total = total + durasi
    banyak = banyak + 1
    durasi = int(input("Waktu proses (menit, -1 selesai :)"))

if banyak == 0:
    print("Belum ada data yang dimasukkan")
else:
    print("Banyak data :", banyak)
    print("Rata rata :", round (total/banyak, 2), "menit")
    
    #Cara membaca

    # Jika input itu selain -1, maka akan terus looping dan setiap tahap looping dihitung
    # Jika input -1, maka looping selesai dan keluar hasil banyak data
  
    # Dalam studi kasus
    # Input1 10 (True), 
    # input2 15 (True), 
    # input3 -1 (False)
    # banyak data 2 didapatkan dari (input1,input2)
    
    # Rata rata = 12.5 menit
    # Rata rata 12.5 menit didapatkan dari (Hasil pembagian 10+15)
