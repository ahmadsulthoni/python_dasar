'''
init berguna untuk memasukan atribut yang akan langsung di rubah saat menginstansiet class
init akan berjalan saat kita membuat class baru,
bedanya dengan methode, jika methode hanya akan berjalan saat di panggil
init sudah berjalan sendiri /menginisialisasi object
'''
#contoh

class mahasiswa():
    def __init__(self,input_nama,input_nim):
        self.nama = input_nama
        self.nim = input_nim

    def belajar(self,kondisi):
        print(self.nama,'sedang belajar',kondisi)

    def tidur(self):
        print(self.nama,'tidur di kelas')

otong = mahasiswa('otong surotong',13317000)

print(otong.nama)
print(otong.nim)
otong.belajar('dengan giat')