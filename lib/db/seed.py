from faker import Faker
from lib.db.session import SessionLocal
from lib.db.models import User, Event, Booking  
import random
faker = Faker()
session = SessionLocal()


session.query(Booking).delete()
session.query(Event).delete()
session.query(User).delete()


users = [User(username=faker.name(), email=faker.email()) for _ in range(5)]
session.add_all(users)
session.commit()

# Create events
events = [Event(title=faker.catch_phrase(), description=faker.text(), event_date=faker.future_date()) for _ in range(5)]

session.add_all(events)
session.commit()

# Create bookings
bookings = [
    Booking(user_id=random.choice(users).id, event_id=random.choice(events).id)
    for _ in range(10)
]
session.add_all(bookings)
session.commit()

print("Database seeded successfully.")
session.close()