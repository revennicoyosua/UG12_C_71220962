x = input("masukan angka:")
y = input("masukan angka yang dihitung:")

hitung = 0

for i in x:
    if i == y:
        hitung += 1

print("Angka",y,"muncul sebanyak",hitung,"kali")
