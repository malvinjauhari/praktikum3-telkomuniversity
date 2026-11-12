total = 0
lulus = 0
remedial = 0
tidak_lulus = 0
tertinggi = 0

print("=== Program Rekap Nilai Kuis Kelas ===")
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah_mahasiswa):
    print(f"\nMasukkan nilai mahasiswa ke-{i+1}:")
    nilai = int(input("Masukkan nilai: "))

    # Perbaikan operator: > 100 (bukan < 100)
    while nilai < 0 or nilai > 100:
        print("Nilai tidak valid, masukkan nilai antara 0-100")
        nilai = int(input("Masukkan nilai kembali: "))

    # Percabangan bertingkat
    if nilai >= 60:
        if nilai >= 85:
            kategori = "Lulus dengan nilai bagus"
        else:
            kategori = "Lulus dengan nilai cukup" 
        lulus += 1
    else:
        if nilai >= 40:
            kategori = "Remedial"
            remedial += 1 
        else:
            kategori = "Tidak lulus"
            tidak_lulus += 1

    print("Kategori :", kategori)

    # Akumulasi total dan pengecekan nilai tertinggi
    total += nilai
    if nilai > tertinggi:
        tertinggi = nilai

# Perhitungan rata-rata dilakukan setelah perulangan 'for' selesai
if jumlah_mahasiswa > 0:
    rata_rata = total / jumlah_mahasiswa
else:
    rata_rata = 0

print("==== REKAP KUIS ====")
print("Rata-rata  :", rata_rata)
print("Tertinggi  :", tertinggi)
print("Lulus      :", lulus)
print("Remedial   :", remedial)
print("Tidak Lulus:", tidak_lulus)
