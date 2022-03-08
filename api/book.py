from fastapi import APIRouter

from services.book import save_book, test_transactional

book_router = APIRouter()


@book_router.get("/save-book/{title}")
def post_books(title):
    return save_book(title)


@book_router.get("/test-transactional")
def _test():
    test_transactional()
    return {'message': "this won't happen :)"}
