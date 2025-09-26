import json

class Book:
    """Класс для представления книги в библиотеке."""

    def __init__(self, title, author, status, genre, score, language):
        """Инициализирует экземпляр книги с заданными атрибутами."""
        self.title = title
        self.author = author
        self.status = status
        self.genre = genre
        self.score = score
        self.language =language

    def __repr__(self):
        """Возвращает строковое представление объекта Book для отладки."""
        return f"Book(title='{self.title}', author='{self.author}')"

    def to_dict(self):
        """Преобразует объект Book в словарь, готовый для сохранения в JSON."""
        return {
            'title': self.title,
            'author': self.author,
            'status': self.status,
            'genre': self.genre,
            'score': self.score,
            'language': self.language
        }

class Library:
    """Класс для управления коллекцией книг."""

    def __init__(self):
        """Инициализирует пустую библиотеку."""
        self.books = []

    def add_book(self, book):
        """Добавляет объект книги в коллекцию библиотеки."""
        self.books.append(book)

    def save_to_file(self, filename='library.json'):
        """Сохраняет список книг в JSON-файл."""
        data_to_save = []
        for book in self.books:
            data_to_save.append(book.to_dict())

        with open(filename, 'w', encoding='utf-8') as f:
            #ensure_ascii=False — для корректного отображения кириллицы.
            #indent=4 — делает файл красивым и читаемым для человека, с отступами.
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)

        print(f"Библиотека успешно сохранена в файл {filename}")

    def load_from_file(self, filename='library.json'):
        """Читает список книг в JSON-файле."""
        # Шаг 1: Ставим "ловушку для ошибок"
        try:
            # Шаг 2: Пробуем открыть файл на чтение ('r')
            with open(filename, 'r', encoding='utf-8') as f:
                # Шаг 3: Загружаем из файла список словарей
                list_of_dicts = json.load(f)
                # Шаг 4: Проходимся циклом по этому списку
                for book_dict in list_of_dicts:
                    # Шаг 5: Для каждого словаря создаем "живой" объект Book
                    new_book = Book(**book_dict)
                    # Шаг 6: Добавляем воссозданную книгу в нашу библиотеку
                    self.add_book(new_book)

            print(f"Библиотека успешно загружена из файла {filename}")
        # Шаг 7: Если в "ловушку" попалась ошибка "Файл не найден"
        except FileNotFoundError:
            # Шаг 8: Просто выводим сообщение и ничего не делаем.
            # Библиотека останется пустой, как и было задумано.
            print(f"Файл {filename} не найден. Создана новая пустая библиотека.")

# 1. Создаем пустую библиотеку
my_library = Library()
# 2. Сразу же пытаемся загрузить в нее данные из файла
my_library.load_from_file()