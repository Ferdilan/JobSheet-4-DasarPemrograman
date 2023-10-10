#Untuk memudahkan input saat running maka jadikan komentar kode yang tidak akan dirunning

#Program Asli
# nilai = int(input("Masukkan sebuah angka: "))

# if nilai >= 100:
#     nilai+=10
# else:
#     nilai-=10
# print("Hasil Nilai akhir adalah", nilai)


#Modifikasi Program
nilai1 = int(input("Masukkan angka pertama: "))
nilai2 = int(input("Masukkan angka kedua: "))

rata = (nilai1 + nilai2)/2

if rata >= 100:
    rata -= 5
print("Hasil rata rata nilai adalah: ", rata)
    