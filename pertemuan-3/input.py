print("==== Program Identifikasi Lamaran Kerja")

while True:
    nama = str(input("Masukkan nama anda, Lalu anda ketik 'selesai' :"))
    if nama.lower() == 'selesai':
        break
gender = str(input("Masukkan gender (L/P)").upper())

if gender == 'L':
    posisi = input("Daftar sebagai teknisi atau driver")
    print("Lamaran", nama, "Anda Sebagai", posisi, "Berhasil diterima? :")
elif gender == 'P':
    posisi = input("Daftar sebagai admin atau resepsionis? :")
    print("Lamaran", nama, "Anda Sebagai", posisi, "Berhasil diterima? :")
else:
    print("Gender Tidak Terdefinisi")

print("==== Sampai Jumpa Lagi ====")