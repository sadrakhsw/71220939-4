def cek_angka(x,y,z):
    if (x != y != z) and (x + y == z or x + z == y or y + z == x):
        return True
    else:
        return False

x = int(input("masukkan angka 1 : "))
y = int(input("masukkan angka 2 : "))
z = int(input("masukkan angka 3 : "))

print(cek_angka(x,y,z))
