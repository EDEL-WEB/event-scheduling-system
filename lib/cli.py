from lib.db import queries, commands
from lib.db.session import SessionLocal

def print_menu():
    print("\n=== Event Scheduling System CLI ===")
    print("1. List all users")
    print("2. List all events")
    print("3. List upcoming events")
    print("4. List all bookings")
    print("5. List bookings for a user")
    print("6. Add a booking")
    print("7. Delete a booking")
    print("8. Update event title")
    print("9. Update event description")
    print("10. View event attendees")
    print("11. Search events by date range")
    print("12. Exit")

def main():
    session = SessionLocal()
    try:
        while True:
            print_menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                queries.list_users(session)

            elif choice == "2":
                queries.list_events(session)

            elif choice == "3":
                queries.list_upcoming_events(session)

            elif choice == "4":
                queries.list_bookings(session)

            elif choice == "5":
                user_id = input("Enter user ID: ").strip()
                if user_id.isdigit():
                    queries.list_bookings_for_user(session, int(user_id))
                else:
                    print("Invalid user ID.")

            elif choice == "6":
                user_id = input("Enter user ID: ").strip()
                event_id = input("Enter event ID: ").strip()
                if user_id.isdigit() and event_id.isdigit():
                    commands.add_booking(session, int(user_id), int(event_id))
                else:
                    print("Invalid input for user or event ID.")

            elif choice == "7":
                booking_id = input("Enter booking ID to delete: ").strip()
                if booking_id.isdigit():
                    commands.delete_booking(session, int(booking_id))
                else:
                    print("Invalid booking ID.")

            elif choice == "8":
                event_id = input("Enter event ID to update: ").strip()
                new_title = input("Enter new event title: ").strip()
                if event_id.isdigit() and new_title:
                    commands.update_event_title(session, int(event_id), new_title)
                else:
                    print("Invalid input.")

            elif choice == "9":
                event_id = input("Enter event ID to update: ").strip()
                new_description = input("Enter new event description: ").strip()
                if event_id.isdigit() and new_description:
                    commands.update_event_description(session, int(event_id), new_description)
                else:
                    print("Invalid input.")

            elif choice == "10":
                event_id = input("Enter event ID to view attendees: ").strip()
                if event_id.isdigit():
                    commands.view_event_attendees(session, int(event_id))
                else:
                    print("Invalid event ID.")

            elif choice == "11":
                start_date = input("Enter start date (YYYY-MM-DD): ").strip()
                end_date = input("Enter end date (YYYY-MM-DD): ").strip()
                if start_date and end_date:
                    queries.search_events_by_date_range(session, start_date, end_date)
                else:
                    print("Both start and end dates are required.")

            elif choice == "12":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

    finally:
        session.close()

if __name__ == "__main__":
    main()
