# TODO Найдите количество книг, которое можно разместить на дискете
book = 100 * 50 * 25 * 4
volume = 1.44 * 1024 * 1024
number_of_books = int(volume // book)
print("Количество книг, помещающихся на дискету:", number_of_books)
