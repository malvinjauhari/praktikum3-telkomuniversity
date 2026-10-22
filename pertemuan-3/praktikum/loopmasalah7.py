#Latihan looping pengelompokan masalah

suhu_tertinggi = None
urutan_tertinggi = 0 
count_lebih_80 = 0
total_suhu_80 = 0
count_suhu_80 = 0


for i in range(1,9):
    suhu = int(input(f"Suhu pencatattan ke - {i}"))


    if suhu_tertinggi is None or suhu > suhu_tertinggi:
        suhu_tertinggi = suhu
        urutan_tertinggi = 1

    if suhu >80 :
        count_lebih_80 +=1
        total_suhu_80 +=1

print (f" Suhu tertinggi: {suhu_tertinggi} (pencatatatn ke =) (urutan_tertinggii)")

if count_lebih_80 == 0:
    print(" Tidak ada suhu yang melebihi 80")
else:
    print(f"suhu melebihi 80 : {count_lebih_80} kali")
    print(f"Rata rata suhu yang melebihi 80 :")
    {total_suhu_80 / count_lebih_80}
