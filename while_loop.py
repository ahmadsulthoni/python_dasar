#contoh 1

'''
angka = 0
while angka < 5:
    print('Nilai angka adalah :', angka)
    angka = angka+1
'''

#contoh 2
start = True
angka = 0

while start:
    print("di dalam while",angka)
    if angka == 100:
        start = False
        print('Oke angka 100 Telah di temukan')
    angka += 1


