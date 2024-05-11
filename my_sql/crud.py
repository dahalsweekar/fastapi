from sqlalchemy.orm import Session
from . import schemas, table


def create_user(db: Session, user: schemas.User):
    db_user = table.User(name=user.name, age=user.age, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_item(db: Session, item: schemas.Item, owner_id: int):
    db_item = table.Item(title=item.title, description=item.description, owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(table.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(table.User).filter(table.User.id == user_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(table.Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int = 0):
    return db.query(table.Item).filter(table.Item.id == item_id).first()


def remove_item(db: Session, item_id: int):
    item = db.query(table.Item).filter(table.Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    else:
        return False


def remove_user(db: Session, user_id: int):
    user = db.query(table.User).filter(table.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    else:
        return False


def update_item(db: Session, item_id: int, new_data: schemas.Item):
    item = db.query(table.Item).filter(table.Item.id == item_id).first()

    if item:
        item.title = new_data.title
        item.description = new_data.description
        db.commit()
        return True
    else:
        return False


def update_user(db: Session, user_id: int, new_data: schemas.User):
    user = db.query(table.User).filter(table.User.id == user_id).first()
    if user:
        user.name = new_data.name
        user.email = new_data.email
        user.age = new_data.age
        db.commit()
        return True
    else:
        return False
