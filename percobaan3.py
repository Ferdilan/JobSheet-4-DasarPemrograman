usia = int(input("Masukkan usia anda: "))

if usia > 60:
    print("Anda lansia.")
elif usia > 45:
    print("Anda tua.")
elif usia > 17:
    print("Anda dewasa.")
elif usia > 5:
    print("Anda Anak-anak.")
#modifikasi
elif usia <= 0:
    print("Umur yang anda masukkan salah")
#endmodifikasi
else:
    print("Anda Balita")

