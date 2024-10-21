disk_cap_in_bytes = 1.44 * 2**20

pages = 100
strings = 50
chars = 25
char_weight = 4

book_weight = pages * strings * chars * char_weight

how_many_books = int(disk_cap_in_bytes / book_weight)

print("Количество книг, помещающихся на дискету:", how_many_books)
