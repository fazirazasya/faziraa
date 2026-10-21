#  Input 
tugas = float(input("masukkan nilai tugas:  "))
uts = float(input("masukkan nilai uts:  "))
uas = float(input("masukkan nilai uas:   "))
kehadiran_mahasiswa = float(input("masukkan persentase kehadiran:  "))

nilai_akhir = (20 / 100 * tugas) * (30 / 100 * uts) * (50 / 100 * uas)

print("=== SISTEM EVALUASI MAHASISWA ===")
print("nilai akhir =", nilai_akhir)
print(kehadiran_mahasiswa, "%")
      
if nilai_akhir >=85 and kehadiran_mahasiswa >=90 and nilai_akhir % 2 == 0:
          print("status  :  LULUS DENGAN PREDIKAT")
elif  nilai_akhir >=75 and kehadiran_mahasiswa >=80:
          print("status  :  LULUS")
else :          
        print ("status   :  TIDAK LULUS")