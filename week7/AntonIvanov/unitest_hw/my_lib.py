class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class BookShelf:
    __books_list = []

    def __len__(self):
        return len(self.__books_list)

    def __add__(self, book: Book):
        self.__books_list.append(book)
        return self

    @property
    def description(self) -> str:
        print_list = [f"{i}. {j.title} - {j.author}" for i, j in enumerate(self.__books_list)]
        return '\n'.join(print_list)

    def take_book(self, index: int):
        try:
            return self.__books_list.pop(index)
        except IndexError:
            return "No such index"


if __name__ == '__main__':
    b = Book('Arthur Canonndale', "Sherlok Holmes")
    b1 = Book('Arthur Canonndale', "Sherlok Holmes")
    bsh = BookShelf()
    bsh += b
    bsh += b1
    print(bsh.description)
    print(bsh.take_book(0))
    print(bsh.take_book(1))
