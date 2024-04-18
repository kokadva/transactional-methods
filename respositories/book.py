from decorators.database import db


@db
def save(book, db):
    db.add(book)
    db.flush()
