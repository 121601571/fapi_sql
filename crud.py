from sqlalchemy.orm import Session

import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_myuser(db: Session, user_id: int):
    return db.query(models.MyUser).filter(models.MyUser.id == user_id).first()


def get_myuser_by_email(db: Session, email: str):
    return db.query(models.MyUser).filter(models.MyUser.email == email).first()

def get_myuser_by_name(db: Session, name: str):
    return db.query(models.MyUser).filter(models.MyUser.username == name).first()


def get_myusers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyUser).offset(skip).limit(limit).all()

def get_password_hash(password):
    return pwd_context.hash(password)

def create_myuser(db: Session, user: schemas.MyUserCreate):
    #fake_hashed_password = user.password + "notreallyhashed"
    fake_hashed_password = get_password_hash(user.password)
    db_user = models.MyUser(email=user.email, password=fake_hashed_password, username = user.username, telnum = user.telnum)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user