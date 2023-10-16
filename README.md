## Wrapper for SQL Alchemy (Private)
<hr>

### Setup
```
pip install git+https://github.com/AlexQ0807/sqlalchemywrapper.git
```


### Example

```
from sqlalchemywrapper.engine import SQLAlchemyEngineWrapper 

CONNECTION_STR = "sqlite:///test.db"

engine_sqlite = SQLAlchemyEngineWrapper.create_engine_from_connection_str(
    connection_string=CONNECTION_STR)
sqlite_wrapper = SQLAlchemyEngineWrapper(engine=engine_sqlite)


# CREATE TABLE
sqlite_wrapper.modify('''
    CREATE TABLE person (
        id INTEGER,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)
    );
''')

# INSERT ROW
sqlite_wrapper.modify('''
    INSERT INTO person (first_name, last_name)
    VALUES ("Patrick", "Star");
''')

# SELECT
print(
    sqlite_wrapper.select('''
            SELECT * FROM person;
    ''', as_list_of_lists=True)
)

```