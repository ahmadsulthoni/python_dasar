#stack adalah penumpukan seperti bentuk buku jadi pengambilanya dari atas dulu (keluarnya di akhir)
#queue antrian seperti antrian di kasir supermarket atau rumah sakit (keluar di akhir)

tumpukan = [1,2,3,4,5,6]
print('data sekarang',tumpukan)

#memasukan data baru
tumpukan.append(7)
print('data masuk', 7)
print('setelah di append ', tumpukan)
tumpukan.append(8)
print('data masuk', 8)
print('setelah di append ', tumpukan)

out = tumpukan.pop()
print('data keluar',out)
print('data sekarang',tumpukan)

#Queue
from collections import deque
antrean = deque([1,2,3,4,5])
print('data sekarang',antrean)