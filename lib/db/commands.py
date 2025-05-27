from lib.db.models import Booking, Event
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from prettytable import PrettyTable

def add_booking(session, user_id, event_id):
    try:
        event = session.query(Event).filter_by(id=event_id).first()
        if not event:
            print(f"❌ Event with ID {event_id} does not exist.")
            return

        booking = Booking(user_id=user_id, event_id=event_id, booking_time=datetime.now())
        session.add(booking)
        session.commit()

        table = PrettyTable(["Booking ID", "User ID", "Event ID", "Booking Time"])
        table.add_row([booking.id, booking.user_id, booking.event_id, booking.booking_time.strftime("%Y-%m-%d %H:%M:%S")])
        print("✅ Booking created successfully:")
        print(table)
    except SQLAlchemyError as e:
        session.rollback()
        print(f"❌ Failed to add booking: {e}")

def delete_booking(session, booking_id):
    try:
        booking = session.query(Booking).filter_by(id=booking_id).first()
        if not booking:
            print("❌ Booking not found")
            return

        session.delete(booking)
        session.commit()
        print(f"✅ Booking ID {booking_id} deleted successfully")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"❌ Failed to delete booking: {e}")

def update_event_title(session, event_id, new_title):
    try:
        event = session.query(Event).filter_by(id=event_id).first()
        if not event:
            print("❌ Event not found")
            return

        old_title = event.title
        event.title = new_title
        session.commit()
        print(f"✅ Event ID {event_id} title updated from '{old_title}' to '{new_title}'")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"❌ Failed to update event: {e}")
