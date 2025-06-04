from prettytable import PrettyTable
from lib.db.models import User, Booking, Event
from datetime import datetime
import random
from sqlalchemy import and_

PLACEHOLDERS = [
    "Community Events Team",
    "Pending Assignment",
    "Awaiting Organizer",
    "Central Office",
    "Events Department",
    "To Be Confirmed",
    "Local Committee",
    "Management Team",
    "Program Coordinator",
    "Temporary Host"
]
placeholders = PLACEHOLDERS

def list_users(session):
    users = session.query(User).all()
    table = PrettyTable()
    table.field_names = ["ID", "Username", "Email"]

    for user in users:
        table.add_row([user.id, user.username, user.email])

    print(table)

def list_events(session):
    events = session.query(Event).all()
    table = PrettyTable(["ID", "Title", "Date", "Organizer"])

    for event in events:
        organizer = event.organizer_id or random.choice(placeholders)
        table.add_row([event.id, event.title, event.event_date.strftime("%Y-%m-%d"), organizer])

    print(table)

def list_upcoming_events(session):
    today = datetime.now().date()
    events = session.query(Event).filter(Event.event_date >= today).order_by(Event.event_date).all()
    table = PrettyTable(["ID", "Title", "Date", "Organizer"])

    for event in events:
        organizer = event.organizer_id or random.choice(placeholders)
        table.add_row([event.id, event.title, event.event_date.strftime("%Y-%m-%d"), organizer])

    print(table)

def list_bookings(session):
    bookings = session.query(Booking).all()
    table = PrettyTable(["Booking ID", "User ID", "Event ID", "Booking Time"])

    for booking in bookings:
        booking_time = booking.booking_time.strftime("%Y-%m-%d %H:%M:%S")
        table.add_row([booking.id, booking.user_id, booking.event_id, booking_time])

    print(table)

def list_bookings_for_user(session, user_id):
    bookings = session.query(Booking).filter(Booking.user_id == user_id).all()
    table = PrettyTable(["Booking ID", "User ID", "Event ID", "Booking Time"])

    for booking in bookings:
        booking_time = booking.booking_time.strftime("%Y-%m-%d %H:%M:%S")
        table.add_row([booking.id, booking.user_id, booking.event_id, booking_time])

    print(table)

def search_events_by_date_range(session, start_date_str, end_date_str):
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    if start_date > end_date:
        print("Start date cannot be after end date.")
        return

    events = session.query(Event).filter(
        and_(
            Event.event_date >= start_date,
            Event.event_date <= end_date
        )
    ).order_by(Event.event_date).all()

    if events:
        table = PrettyTable(["ID", "Title", "Date", "Organizer"])
        for event in events:
            organizer = event.organizer_id or random.choice(placeholders)
            table.add_row([event.id, event.title, event.event_date.strftime("%Y-%m-%d"), organizer])
        print(table)
    else:
        print(f"No events found between {start_date_str} and {end_date_str}.")
