#contoh 1

'''
angka = 0
while angka < 5:
    print('Nilai angka adalah :', angka)
    angka = angka+1


#contoh 2
start = True
angka = 0

while start:
    print("di dalam while",angka)
    if angka == 100:
        start = False
        print('Oke angka 100 Telah di temukan')
    angka += 1
'''
#contoh 3
#else,break,continue,pass

angka = 0

while angka<10:
    if angka == 5:
        pass
    print('Nilai angka adalah',angka)
    angka = angka + 1
    print('Nilai angka di akhir while adalah ',angka)


