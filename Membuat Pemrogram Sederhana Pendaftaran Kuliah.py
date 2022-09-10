#Input
from functools import total_ordering


Nama=input("Input Nama : ")
Nis=input("Input NIS : ")
jurusan=input("Input Jurusan [SI/SIA] : ")
#Proses
if jurusan=="SI":
    namajurusan="Sistem Informasi"
    harga=2400000
else:
    jurusan=="SIA"
    namajurusan="Sistem Informasi Akutansi"
    harga=2000000
    
#Input Jumlah Beli
jumlah=int(input("Masukkan Jumlah Beli : "))

#Cetak Hasil
print("------------------------------------")
print(" PEMBAYARAN BIAYA KULIAH")
print("------------------------------------")
print("Nama Pembeli : "+str(Nama))
print("NIS : "+str(Nis))
print("Kode Jurusan yang dipilih : "+str(jurusan))
print("Nama Kota Tujuan : "+str(namajurusan))
print("Harga : ",+(harga))
print("Jumlah Beli : ",+(jumlah))
print("------------------------------------")

total=harga*jumlah
print("Total Bayar : ",+(total))
ubay=int(input("Masukkan Uang Bayar : "))
uangkembali=ubay-total
print("Uang Kembali : ",+uangkembali)