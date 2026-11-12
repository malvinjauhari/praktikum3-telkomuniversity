umur = int(input("Masukkan Umur: "))
kartu_pelajar = input("Apakaah memiliki kartu pelajar? ")

if umur >= 17:
    print("Umur memenuhi syarat nonton film 17++")
    if kartu_pelajar == "ya":
        print("Tiket: Harga pelajar Rp.30.000")
    else:
        print("Tiket : harga umum Rp. 45.000")
else:
    print("Maaf, film ini khusus usia 17 Tahun")
