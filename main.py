class Book:
    # 1. Тебе понадобится добавить ещё жанр, оценка прочитанного (0-10 баллов), язык книги
    def __init__(self, title, author, status, genre, score, language):
        self.title = title
        self.author = author
        self.status = status
        self.genre = genre
        self.score = score
        self.language =language

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

book1 = Book("Унесенные ветром", "Маргарет Митчелл", "Прочитано", "Роман", 10, "Русский")
book2 = Book("Тим Талер, или Проданный смех", "Джеймс Крюс", "Прочитано", "Повесть", 10, "Русский")
print(book1, book2)

my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)
print(my_library.books)

# Советы и вопросы
# 2. Не путай словари и объекты. Понятно, почему ты их путаешь, но проясни разницу в своей голове. Это крайне важно
# 3. В гитхаб тебе нужно сделать так же, как ты делала в проектe бота для телеграм - protected main branch и ветки под features
# 4. ответь себе на вопрос - зачем нужны переменные класса и переменные экземпляра
# 5. как это связано с конструктором?
# 6. Markdown включается с помощью ``` ```

