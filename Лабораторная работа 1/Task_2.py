# TODO Найдите количество книг, которое можно разместить на дискете
book = 100*50*25*4
vol = 1.44*1024*1024
val = int(vol//book)
print("Количество книг, помещающихся на дискету:", val)
