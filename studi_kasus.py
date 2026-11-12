# Konstanta
TARGET = 100
PENANDA = -1

# Inisialisasi variabel awal
banyak_hari = 0
total_produksi = 0
hari_target = 0
tertinggi = 0
hari_tertinggi = 0
terendah = None  # Tidak diisi 0 agar tidak mengganggu pencarian nilai minimum
hari_terendah = 0

# Baca produksi hari ke-1 sebelum perulangan (Pola Sentinel / Penanda)
produksi = int(input(f"Produksi hari ke-{banyak_hari + 1} ({PENANDA} untuk selesai): "))

while produksi != PENANDA:
    banyak_hari += 1
    total_produksi += produksi

    # Hitung hari mencapai target
    if produksi >= TARGET:
        hari_target += 1

    # Memperbarui nilai tertinggi dan terendah dan harinya
    if banyak_hari == 1:
        tertinggi = produksi
        hari_tertinggi = banyak_hari
        terendah = produksi
        hari_terendah = banyak_hari
    else:
        if produksi > tertinggi:
            tertinggi = produksi
            hari_tertinggi = banyak_hari
        if produksi < terendah:
            terendah = produksi
            hari_terendah = banyak_hari

    # Baca produksi hari berikutnya di akhir blok while
    produksi = int(input(f"Produksi hari ke-{banyak_hari + 1} ({PENANDA} untuk selesai): "))

# Output Rekap Produksi
print("=== REKAP PRODUKSI ===")
if banyak_hari == 0:
    print("Belum ada data produksi.")
else:
    rata_rata = total_produksi / banyak_hari
    print(f"Banyak hari : {banyak_hari}")
    print(f"Total produksi : {total_produksi}")
    print(f"Rata-rata per hari: {rata_rata:.2f}")
    print(f"Hari mencapai target ({TARGET}): {hari_target}")
    print(f"Tertinggi: {tertinggi} unit (hari ke-{hari_tertinggi})")
    print(f"Terendah : {terendah} unit (hari ke-{hari_terendah})")
