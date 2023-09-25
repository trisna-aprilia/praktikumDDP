# data
print("==========LOGIN==========")
nama = (input("nama :"))
nim = (input("nim :"))
kelas = (input("kelas :"))
password = (input("password :"))
print("=========================")

print("PROGRAM KONVERSI SATUAN MASSA KILOGRAM")
# input berat
kg = float(input("Masukkan nilai dalam kilogram: "))
pilihan = input("Masukkan pilihan satuan massa (1/2/3): ")

# konversi ke pounds(lb)
if pilihan == "1" :
    nilai = kg * 2.20462
    print(f"{kg} kilogram sama dengan {nilai} pounds(lb)")
# konversi ke ounce(ons)
elif pilihan == "2" :
    nilai = kg * 35.274
    print(f"{kg} kilogram sama dengan {nilai} ounce(ons)")
# konversi ke gram(g)
elif pilihan == "3" :
    nilai = kg * 1000
    print(f"{kg} kilogram sama dengan {nilai} gram(g)")
# jika pilihan bukan 1/2/3
else:
    print("pilihan tidak valid masukkan pilihan yang benar. Pilih 1, 2, atau 3")
