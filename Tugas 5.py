totalbelanja = float(input("Masukkan Total Belanja: "))
if totalbelanja > 1000000:
    print("Anda mendapatkan potongan member platinum sebesar 10%")
    totalbelanja_diformat = '{:,}'.format(totalbelanja)
    print("Total Belanja anda adalah: ", totalbelanja_diformat)
    potongan = 0.1 * totalbelanja
    potongan_diformat = '{:,}'.format(potongan)
    print("Potongan harga anda sebanyak: ", potongan_diformat)
    totalbayar = totalbelanja - potongan
    totalbayar_diformat = '{:,}'.format(totalbayar)
    print("Total bayar anda adalah: ", totalbayar_diformat)
elif totalbelanja > 500000:
    print("Anda mendapatkan potongan member platinum sebesar 5%")
    totalbelanja_diformat = '{:,}'.format(totalbelanja)
    print("Total Belanja anda adalah: ", totalbelanja_diformat)
    potongan = 0.05 * totalbelanja
    potongan_diformat = '{:,}'.format(potongan)
    print("Potongan harga anda sebanyak: ", potongan_diformat)
    totalbayar = totalbelanja - potongan
    totalbayar_diformat = '{:,}'.format(totalbayar)
    print("Total bayar anda adalah: ", totalbayar_diformat)
else:
    print("Anda mendapatkan potongan member silver sebesar 2%")
    totalbelanja_diformat = '{:,}'.format(totalbelanja)
    print("Total Belanja anda adalah: ", totalbelanja_diformat)
    potongan = 0.02 * totalbelanja
    potongan_diformat = '{:,}'.format(potongan)
    print("Potongan harga anda sebanyak: ", potongan_diformat)
    totalbayar = totalbelanja - potongan
    totalbayar_diformat = '{:,}'.format(totalbayar)
    print("Total bayar anda adalah: ", totalbayar_diformat)
#_diformat untuk memudahkan membaca output