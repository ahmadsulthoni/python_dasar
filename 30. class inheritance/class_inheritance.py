'''
jangan lakukan DRY = don't repeat your self
artinya = jangan mengulang apa yang telah di lakukan
'''

class ojek():

    def __init__(self,nama,transmisi,daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_abang (self):
        print('nama',self.nama,'\nmotor',self.transmisi,'\ndaerah',self.daerah)

class gojek(ojek):
    def cek_id_abang(self):
        print('cek aplikasi gojek')

ojek1 = ojek('mario','manual','bandung selatan')
ojek2 = gojek('jackson','automatic','tasikmalaya')

ojek1.cek_id_abang()
ojek2.cek_id_abang()