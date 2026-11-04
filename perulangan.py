print("=== SISTEM PENILAIAN MAHASISWA ===")

jumlah = int(input("Masukkan jumlah mahasiswa (5-10): "))

if jumlah >= 5 and jumlah <= 10:
    total_nilai = 0

    for i in range(1, jumlah + 1):
        nilai = float(input(f"Masukkan nilai mahasiswa {i}: "))

        if nilai >= 0 and nilai <= 100:
            total_nilai += nilai
        else:
            print("Nilai harus antara 0-100!")
            break

    else:
        rata_rata = total_nilai / jumlah

        print("\n=== HASIL PENILAIAN ===")
        print("Jumlah mahasiswa:", jumlah)
        print("Total nilai:", total_nilai)
        print("Nilai rata-rata:", rata_rata)

else:
    print("Jumlah mahasiswa harus antara 5-10!")
