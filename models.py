import logging
from TodoApp.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
    phone_number = Column(String)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info(f"New User created: {self.username}, {self.email}")

class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info(f"New Todo created: {self.title} (Priority: {self.priority})")
