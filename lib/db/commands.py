from .models import Booking, Event, User

def add_booking(session, user_id, event_id):
    user = session.query(User).filter_by(id=user_id).first()
    event = session.query(Event).filter_by(id=event_id).first()

    if not user or not event:
        print("User or event not found.")
        return

    # Prevent duplicate booking
    existing_booking = session.query(Booking).filter_by(user_id=user_id, event_id=event_id).first()
    if existing_booking:
        print("User already booked for this event.")
        return

    # Check capacity limit
    if event.capacity is not None and len(event.bookings) >= event.capacity:
        print(f"Cannot book: Event '{event.title}' has reached its capacity ({event.capacity}).")
        return

    booking = Booking(user_id=user_id, event_id=event_id)
    session.add(booking)
    session.commit()
    print(f"Booking added for user {user_id} to event {event_id}")

def delete_booking(session, booking_id):
    booking = session.query(Booking).filter_by(id=booking_id).first()
    if booking:
        session.delete(booking)
        session.commit()
        print(f"Booking ID {booking_id} deleted.")
    else:
        print("Booking not found.")

def update_event_title(session, event_id, new_title):
    event = session.query(Event).filter_by(id=event_id).first()
    if event:
        old_title = event.title
        event.title = new_title
        session.commit()
        print(f"Event ID {event_id} title updated from '{old_title}' to '{new_title}'")
    else:
        print(f"No event found with ID {event_id}")

def update_event_description(session, event_id, new_description):
    event = session.query(Event).filter_by(id=event_id).first()
    if event:
        old_description = event.description
        event.description = new_description
        session.commit()
        print(f"Event ID {event_id} description updated from '{old_description}' to '{new_description}'")
    else:
        print(f"No event found with ID {event_id}")

def view_event_attendees(session, event_id):
    event = session.query(Event).filter_by(id=event_id).first()
    if not event:
        print(f"No event found with ID {event_id}")
        return

    if not event.bookings:
        print(f"No attendees for event '{event.title}'")
        return

    print(f"Attendees for event '{event.title}':")
    for booking in event.bookings:
        print(f"- {booking.user.username} (ID: {booking.user.id})")
