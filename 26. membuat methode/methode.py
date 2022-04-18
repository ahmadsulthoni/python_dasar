'''
methode adalah sesuatu yang berlaku saat di set / di panggil fungsinya (berjalan saat di panggil)
'''

#class
class mahasiswa():
    nama = 'nama'

    def belajar(self,kondisi):
        print(self.nama,'Sedang belajar',kondisi)

    def tidur(self,kondisi):
        print(self.nama,'Tidur di kelas',kondisi)

#main program
otong = mahasiswa()
ucup = mahasiswa()

otong.nama = 'otong surotong'
ucup.nama = 'michel ucup'

otong.belajar('dengan giat')
ucup.tidur('sambil ngorok')