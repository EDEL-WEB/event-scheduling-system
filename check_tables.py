from sqlalchemy import create_engine, inspect

engine = create_engine('sqlite:///./event_scheduling.db')
inspector = inspect(engine)
print("Tables in database:", inspector.get_table_names())
