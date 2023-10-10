nuas = float(input("Masukkan nilai UAS: "))
nuts = float(input("Masukkan nilai UTS: "))
nkuis = float(input("Masukkan nilai Kuis: "))
ntugas = float(input("Masukkan nilai Tugas: "))

nAkhir = 0.4 * nuas + 0.3 * nuts + 0.1 * nkuis + 0.2 * ntugas

print("Nilai akhir siswa: ", nAkhir)

if nAkhir < 65:
    print("Siswa Remidi")
else:
    print("Siswa Tidak Remidi")
    