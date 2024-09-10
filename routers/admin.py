import logging
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from TodoApp.models import Todos
from TodoApp.database import SessionLocal
from .auth import get_current_user

# Set up logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        logger.warning(f"Unauthorized access attempt by user: {user}")
        raise HTTPException(status_code=401, detail='Authentication Failed')
    
    logger.info(f"Admin user: {user['username']} reading all todos.")
    todos = db.query(Todos).all()
    logger.info(f"{len(todos)} todos retrieved by admin user: {user['username']}")
    return todos


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        logger.warning(f"Unauthorized delete attempt by user: {user}")
        raise HTTPException(status_code=401, detail='Authentication Failed')
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        logger.warning(f"Todo with ID {todo_id} not found for deletion by admin user: {user['username']}")
        raise HTTPException(status_code=404, detail='Todo not found.')
    
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
    logger.info(f"Todo with ID {todo_id} deleted by admin user: {user['username']}")
