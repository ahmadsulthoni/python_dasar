'''
di gunakan untuk private attribut supaya tidak dapat akses dari luar
contoh syntax
__nilai = 0
'''

class mahasiswa():
    jurusan = 'Teknik tataboga'
    __nilai = 0 #private

    def __init__(self,input_nama,input_nim):
        self.nama = input_nama #public
        self.nim = input_nim #public

    def uts(self,input_nilai):
        self.__nilai += input_nilai

    def uas(self,input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,'Tidak lulus')
        else:
            print(self.nama,'lulus')

otong = mahasiswa('otong surotong',13317001)
ucup = mahasiswa('Michel ucup',13317002)
otong.uts(15)
otong.uas(50)
otong.check_status()
ucup.uts(5)
ucup.uas(25)
ucup.check_status()