from decorators.database import db
from schemas.book import BookInfo


@db
def save(book, db):
    db.add(book)
    db.flush()
    return BookInfo.from_orm(book)
