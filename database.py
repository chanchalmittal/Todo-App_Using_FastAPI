import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Set up logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# Log the database connection attempt
logger.info(f"Connecting to the database at {SQLALCHEMY_DATABASE_URL}")

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
    logger.info("Database connection established successfully.")
except Exception as e:
    logger.error(f"Failed to connect to the database: {e}")
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
logger.info("SessionLocal configured for database sessions.")

Base = declarative_base()
logger.info("Base declarative class created.")
