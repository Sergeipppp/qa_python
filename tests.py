from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    book1name = 'Гордость и предубеждение и зомби'
    book2name = 'Что делать, если ваш кот хочет вас убить'
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book(self.book1name)
        collector.add_new_book(self.book2name)

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_one_book_and_check_not_set_genre(self):
        collector4 = BooksCollector()
        collector4.add_new_book(self.book1name)
        assert collector4.get_book_genre(self.book1name) == ''

    @pytest.mark.parametrize('name',['','aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'])
    def test_add_new_book_add_book_with_zero_name_with_41_symbols_name_and_more_than_41_symbols_name_false(self, name):
        collector1 = BooksCollector()       
        collector1.add_new_book(name)
        assert len(collector1.get_books_genre()) == 0

    def test_set_book_genre_add_new_book_and_set_not_existing_genre(self):
        collector2 = BooksCollector()
        collector2.add_new_book(self.book1name)
        collector2.set_book_genre(self.book1name,'Драма')
        assert collector2.get_book_genre(self.book1name) != 'Драма'

    def test_set_book_genre_add_one_book_and_set_genre_which_exist(self):
        collector3 = BooksCollector()
        collector3.add_new_book(self.book1name)
        collector3.set_book_genre(self.book1name, 'Фантастика')
        assert collector3.get_book_genre(self.book1name) == 'Фантастика'

    def test_get_books_with_specific_genre_add_three_books_with_two_same_genre(self):
        collector5 = BooksCollector()
        test_value = [(self.book1name, 'Фантастика'),(self.book2name, 'Фантастика'),('Капитан', 'Детективы')] 
        for name, genre in test_value:
            collector5.add_new_book(name)
            collector5.set_book_genre(name,genre)
        assert collector5.get_books_with_specific_genre('Фантастика') == [self.book1name, self.book2name]

    def test_get_books_for_children_add_two_books_with_one_genre_for_children(self):
        collector6 = BooksCollector()
        test_value = [(self.book1name, 'Фантастика'),(self.book2name, 'Ужасы')] 
        for name, genre in test_value:
            collector6.add_new_book(name)
            collector6.set_book_genre(name,genre)
        assert collector6.get_books_for_children() == [self.book1name]

    def test_add_book_in_favorites_get_list_of_favorites_books_add_one_book_to_favorites(self):
        collector7 = BooksCollector()
        collector7.add_new_book(self.book1name)
        collector7.add_book_in_favorites(self.book1name)
        assert collector7.get_list_of_favorites_books() == [self.book1name]

    def test_add_book_in_favorites_delete_book_from_favorites_add_one_book_to_favorites_and_delete_it(self):
        collector8 = BooksCollector()
        collector8.add_new_book(self.book2name)
        collector8.add_book_in_favorites(self.book2name)
        collector8.delete_book_from_favorites(self.book2name)
        assert collector8.get_list_of_favorites_books() == []
   
    def test_add_book_in_favorites_add_two_similar_book_to_favorites_and_recieve_only_one(self):
        collector7 = BooksCollector()
        collector7.add_new_book(self.book1name)
        collector7.add_book_in_favorites(self.book1name)
        collector7.add_book_in_favorites(self.book1name)
        assert collector7.get_list_of_favorites_books() == [self.book1name]
