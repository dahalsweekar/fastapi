from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import crud, table, schemas
from .database import SessionLocal, engine

table.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/users')
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_users = crud.get_users(db=db, skip=skip, limit=limit)
    if not db_users:
        raise HTTPException(status_code=404, detail="Users not found")
    return db_users


@app.get('/users/items')
def get_user_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    db_items = crud.get_items(db=db, skip=skip, limit=limit)
    if not db_items:
        raise HTTPException(status_code=404, detail="Items not found")
    return db_items


@app.get('/users/{user_id}')
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get('/users/items/{item_id}')
def get_item_by_id(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="item does not exist")


@app.post('/users/')
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.post('/users/{user_id}/items')
def create_item(item: schemas.Item, user_id: int, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item, owner_id=user_id)


@app.delete('/users/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.remove_user(db=db, user_id=user_id)


@app.delete('/users/items/{item_id}')
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.remove_item(db=db, item_id=item_id)


@app.put('/users/{user_id}')
def update_user(user_id: int, new_data: schemas.User, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user_id=user_id, new_data=new_data)


@app.put('/users/items/{item_id}')
def update_item(item_id: int, new_data: schemas.Item, db: Session = Depends(get_db)):
    item = crud.get_item(db=db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item does not exist")
    return crud.update_item(db=db, item_id=item_id, new_data=new_data)
