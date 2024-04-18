from decorators.database import transactional
from models.book import BookModel
from respositories.book import save
from schemas.book import BookInfo


@transactional
def save_book(title):
    book = save(BookModel(title=title))
    # Return Pydantic model from service (recommended)
    return BookInfo.from_orm(book)


@transactional
def test_transactional():
    save(BookModel(title='test1'))
    1 / 0
    save(BookModel(title='test2'))
