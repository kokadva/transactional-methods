from decorators.database import transactional
from models.book import BookModel
from respositories.book import save
from schemas.book import BookInfo


@transactional
def save_book(title):
    book_model = BookModel(title=title)
    save(book_model)
    book_info = BookInfo.from_orm(book_model)
    return book_info


@transactional
def test_transactional():
    save(BookModel(title='test1'))
    1 / 0
    save(BookModel(title='test2'))
