from decorators.database import transactional
from models.book import BookModel
from respositories.book import save


@transactional
def save_book(title):
    return save(BookModel(title=title))


@transactional
def test_transactional():
    save(BookModel(title='test1'))
    1 / 0
    save(BookModel(title='test2'))
