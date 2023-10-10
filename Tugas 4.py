gajipokok = int(input("Masukkan Gaji Pokok: "))
uangmakan = int(input("Masukkan Uang Makan: "))
uangtransport = int(input("Masukkan Uang Trasnport: "))

totalgaji = gajipokok + uangmakan + uangtransport

if totalgaji >= 1000000:
    pajak = 0.1 * totalgaji
else:
    pajak = 0

gajibersih = totalgaji - pajak
#diformat untuk memudahkan dalam membaca output program
gajibersih_diformat = '{:,}'.format(gajibersih)
pajak_diformat = '{:,}'.format(pajak)
totalgaji_diformat = '{:,}'.format(totalgaji)

print("Total Gaji: ", totalgaji_diformat)
print("Pajak: ", pajak_diformat)
print("Gaji Bersih: ", gajibersih_diformat)