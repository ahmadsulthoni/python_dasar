data = [1,4,9,16,25,36,49,64]
#mengakses list

subdata1 = data[3]
print(subdata1)
subdata2 = data[-3]
print(subdata2)

#memotong list
subdata3 = data[2:4]
print(subdata3)
subdata4 = data[-4:] #: di gunakan untuk mengambil semua
print(subdata4)
subdata5 = data[:4]
print(subdata5)
data2 = [100,200,300,400,500,600,700,800]

#menambah data
data3 = data = data2
print(data3)

#merubah content dari list
data[4] = 87
print(data)
a = data
print(a[4])
#untuk mencopi dengan data
a = data[:]
#merubah content list dengan metode slicing
data[3:5] = [11,12]
print(data)
#list dalam list
x = [data,data2]
print(x)
#mengakses list dalam multi dimentional list
y = x[1][4]
print(x)
print(y)

#methods untuk list
data.append(30)
print(data)

#fungsion yang bisa di gunakan kepada list

panjang_list = len(data)
print(panjang_list)
