# Python ORM with MySQL - Getting Started

This guide will help you get started with Python Object-Relational Mapping (ORM) using SQLAlchemy for MySQL databases.

## Prerequisites

- **Python:** [Download and Install Python](https://www.python.org/downloads/)
- **MySQL:** [Download and Install MySQL](https://dev.mysql.com/downloads/) (*community server*)
- **pip:** Install it using [these instructions](https://pip.pypa.io/en/stable/installation/).

## Setup

1. Create a Python project directory.

2. Set up a virtual environment:
   - Windows: `python -m venv venv`
   - macOS/Linux: `python3 -m venv venv`
   - Activate the environment:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`

3. Install required packages:

```python
pip install SQLAlchemy mysqlclient
```
## Connecting to MySQL

1. Define your database URL:
```python
db_url = "mysql://username:password@localhost/database_name"
```
Replace `username`, `password`, `localhost,` and `database_name` with your MySQL credentials.  

#### Create an engine and session:  
```python
from sqlalchemy import create_engine, sessionmaker
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
```  

### Create A Model  
#### 1.Define your model as a Python class:  
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100))
```

#### 2.Create the table in the database:
```python
Base.metadata.create_all(engine)
```

### Closing the Session
Remember to always cloe the session when done:
```python
session.close()
```  

These are some of the basics needed to get started in with ORMs using python and modules such as SQLAlchemy and MySQLdb.  

**Happy Coding!** 😎