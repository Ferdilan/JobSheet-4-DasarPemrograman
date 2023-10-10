angka1 = float(input("Masukkan sebuah angka pertama: "))
angka2 = float(input("Masukkan sebuah angka kedua: "))
operator = input("Masukkan Operator (+, -, *, /): ")

if operator == '+':
    hasil = angka1 + angka2
    print(angka1, "+", angka2, "=", hasil)
elif operator == '-':
    hasil = angka1 - angka2
    print(angka1, "-", angka2, "=", hasil)
elif operator == '*':
    hasil = angka1 * angka2
    print(angka1, "*", angka2, "=", hasil)
elif operator == '/':
    if angka2 == 0:
        print("Pembagian nol tidak diperbolehkan.")
    else:
        hasil = angka1 / angka2
        print(angka1,"/", angka2, "=", hasil)
else:
    print("Operator tidak valid")
