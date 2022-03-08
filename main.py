import uvicorn
from fastapi import FastAPI

from api.book import book_router
from extensions.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {'message': 'transactional <3'}


app.include_router(book_router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
