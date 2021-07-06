"""
Program untuk menentukan tahun kabisat
jika tahun habis dibagi 4, maka itu tahun kabisat
jika awal abad (1800, 1900, 2000) habis dibagi 400, maka itu tahun kabisat
"""


def tahun_kabisat(tahun):
    kabisat = False
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            kabisat = True
    
    else:
        if (tahun % 4) == 0:
            kabisat = True
    
    return kabisat
    

tahun = int(input('Masukkan Tahun : '))
hasil = tahun_kabisat(tahun)
if hasil:
    if tahun % 100 == 0:
        print('Tahun {} adalah Tahun Kabisat ke {} per 400 tahun dan ke {} per 4 tahun'.format(tahun, int(tahun / 400), int(tahun / 4)))
    else:
        print('Tahun {} adalah Tahun Kabisat ke {} per 4 tahun'.format(tahun, int(tahun / 4)))
    
else:
    print('Tahun {} bukan Tahun Kabisat'.format(tahun))
