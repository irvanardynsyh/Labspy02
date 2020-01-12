# Tugas Praktikum 2 / labspy02
print("========================="
      "\nMENCARI BILANGAN TERBESAR"
      "\n=========================")

a = int (input("Masukkan bilangan pertama : "))
b = int (input("Masukkan bilangan kedua : "))
c = int (input("Masukkan bilangan ketiga : "))

# Mencari Bilangan Terbesar Tunggal
if a > b and a > c:
    terbesar = a
    bilangan = "Bilangan pertama"
elif b > a and b > c:
    terbesar = b
    bilangan = "Bilangan kedua"
elif c > a and c > b:
    terbesar = c
    bilangan = "Bilangan ketiga"

# Mencari Bilangan Terbesar Ganda
elif a == b and a != c:
    terbesar = a
    bilangan = "Bilangan pertama dan kedua"
elif a == c and a != b:
    terbesar = c
    bilangan = "Bilangan kedua dan ketiga"
elif b == c and b != a:
    terbesar = b
    bilangan = "Bilangan ketiga dan pertama"

# Keseluruhan Bilangan Terbesar
elif a and b and c == a and b and c:
    terbesar = a
    bilangan = "Ketiga bilangan tersebut"
else:
    terbesar = 'ERROR'
    bilangan = 'ERROR'

print("Bilangan yang terbesar adalah", bilangan,"dengan nilai", terbesar)