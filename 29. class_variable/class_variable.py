'''
variable yang dimiliki oleh class
sesuatu yang ada self-nya adaah intanses yang tidak ada selfnya milik class

dictionary = mengambil semua komponen dari suatu data
'''

class mahasiswa():

    jumlah_mahasiswa = 0
    def __init__(self,input_nama,input_nim):
        self.nama = input_nama
        self.nim = input_nim
        mahasiswa.jumlah_mahasiswa += 1

otong = mahasiswa('otong surotong',13317001)
ucup = mahasiswa('Michel ucup',13317002)
casandra = mahasiswa('casandra aja',13317003)

print(mahasiswa.jumlah_mahasiswa)