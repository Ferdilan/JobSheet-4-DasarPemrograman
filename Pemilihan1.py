angka = int(input("Masukkan sebuah angka: "))
angka2 = int(input("Masukkan sebuah angka : "))

if angka % 2 == 0:
    print(angka, "adalah bilangan genap. ")
else:
    print(angka, "adalah bilangan ganjil. ")

# modifikasi
if angka2 ^ 1 == angka2 + 1:
    print(angka2, "adalah bilangan genap. ")
else:
    print(angka2, "adalah bilangan ganjil. ")