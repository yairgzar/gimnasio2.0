from sqlalchemy import Session
from models import users

def get_users(db: Session, skip: int = 0, limit: = 10):
    return db.query(users)