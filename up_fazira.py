data_mahasiswa = []
lulus = 0
tidak_lulus = 0

jumlah = int(input("Jumlah mahasiswa: "))

i = 1
while i <= jumlah:
    print("\nData mahasiswa ke-", i)

    nama = input("Nama mahasiswa: ")
    nilai = int(input("Nilai mahasiswa: "))

    if 85 <= nilai <= 100:
        grade = "A"
        keterangan = "Sangat Baik"
        lulus += 1
    elif 75 <= nilai < 85:
        grade = "B"
        keterangan = "Baik"
        lulus += 1
    elif 60 <= nilai < 75:
        grade = "C"
        keterangan = "Cukup"
        lulus += 1
    elif 0 <= nilai < 60:
        grade = "D"
        keterangan = "Tidak Lulus"
        tidak_lulus += 1
    else:
        grade = "-"
        keterangan = "Nilai tidak valid"

    data_mahasiswa.append([nama, nilai, grade, keterangan])
    i += 1

print("\n===== HASIL PENILAIAN =====")

for data in data_mahasiswa:
    print("Nama       :", data[0])
    print("Nilai      :", data[1])
    print("Grade      :", data[2])
    print("Keterangan :", data[3])
    print("--------------------------")

print("Jumlah Lulus      :", lulus)
print("Jumlah Tidak Lulus:", tidak_lulus)