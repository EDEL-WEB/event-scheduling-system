from .models import Booking, Event, User

def add_booking(session, user_id, event_id):
    user = session.query(User).filter_by(id=user_id).first()
    event = session.query(Event).filter_by(id=event_id).first()
    if user and event:
        booking = Booking(user_id=user_id, event_id=event_id)
        session.add(booking)
        session.commit()
        print(f"Booking added for user {user_id} to event {event_id}")
    else:
        print("User or event not found.")

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
