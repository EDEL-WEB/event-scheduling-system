from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    events = relationship("Event", back_populates="organizer", cascade="all, delete-orphan")
    bookings = relationship("Booking", back_populates="user", cascade="all, delete-orphan")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    organizer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(Text)
    event_date = Column(DateTime, nullable=False)
    location = Column(String(100))
    organizer_id = Column(Integer, ForeignKey("users.id"))

    organizer = relationship("User", back_populates="events")
    bookings = relationship("Booking", back_populates="event", cascade="all, delete-orphan")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    booking_time = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="bookings")
    event = relationship("Event", back_populates="bookings")
