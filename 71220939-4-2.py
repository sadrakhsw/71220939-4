def cek_digit_belakang(x,y,z):
    x_modulo = x%10
    y_modulo = y%10
    z_modulo = z%10
    if x_modulo  == y_modulo or x_modulo == z_modulo or y_modulo  == z_modulo:
        return True
    else:
        return False

#input
inp1 = int(input("masukkan input 1: "))
inp2 = int(input("masukkan input 2: "))
inp3 = int(input("masukkan input 3: "))

#output
print(cek_digit_belakang(inp1,inp2,inp3))
