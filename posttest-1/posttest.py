# data
print("==========LOGIN==========")
nama = (input("nama :"))
nim = (input("nim :"))
kelas = (input("kelas :"))
password = (input("password :"))
print("=========================")

print("======konversi satuan massa kilogram=====")
# input massa
kilogram = float(input("masukkan kilogram:"))
pilihan = float(input("masukkan pilihan (1/2/3):"))


# pounds
if pilihan == 1:
    hasil = kilogram * 2.20462
    print(kilogram,"*",2.20462,"=",hasil )

# ons
elif pilihan == 2:
    hasil = kilogram * 35.274
    print(kilogram,"*",35.274,"=",hasil )

# gram
elif pilihan == 3:
    hasil = kilogram * 1000
    print(kilogram,"*",1000,"=",hasil )

else:
    print("pilihan tidak valid masukkan pilihan yang benar. Pilih 1, 2, atau 3")

