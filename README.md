
# Event Scheduling System

A Command-Line Interface (CLI) application for managing users, events, and bookings. This tool allows users to view, create, and modify event data through a simple menu system.


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [CLI Menu Options](#cli-menu-options)
- [File Descriptions](#file-descriptions)
- [Function Descriptions](#function-descriptions)
- [Models](#models)
- [Technologies Used](#technologies-used)
- [Resources](#resources)


## Overview

This project is a lightweight event scheduling system that runs in the terminal. It allows users to manage a list of users, events, and their associated bookings using an SQLite database via SQLAlchemy ORM.

---

## Features

- View all users, events, bookings
- View upcoming events
- Add and remove bookings
- Update event titles
- Filter bookings by user

## Installation

1. Clone the repository:


git clone https://github.com/EDEL-WEB/event-scheduling-system.git
cd event-scheduling-system
Install dependencies:

pip install -r requirements.txt
Set up your database:


alembic upgrade head
Usage
Run the CLI using:

python -m lib.cli
Follow the menu to select your operation.

CLI Menu Options

=== Event Scheduling System CLI ===
1. List all users
2. List all events
3. List upcoming events
4. List all bookings
5. List bookings for a user
6. Add a booking
7. Delete a booking
8. Update event title
9. Exit
File Descriptions
lib/cli.py
This is the main entry point for the CLI app. It initializes the database session and presents the user with a numbered menu. Based on input, it calls the corresponding functions from queries.py and commands.py.

lib/db/queries.py
Contains helper functions that query the database and print data using PrettyTable.

list_users(session): Lists all users.

list_events(session): Lists all events.

list_upcoming_events(session): Shows upcoming events based on today’s date.

list_bookings(session): Lists all bookings.

list_bookings_for_user(session, user_id): Filters bookings by user.

lib/db/commands.py
Contains functions that modify data:

add_booking(session, user_id, event_id): Adds a new booking.

delete_booking(session, booking_id): Deletes a booking.

update_event_title(session, event_id, new_title): Updates an event’s title.

lib/db/models.py
Defines the database models using SQLAlchemy ORM:

User: Represents a user with id, username, and email.

Event: Represents an event with id, title, event_date, and organizer_id.

Booking: Represents a booking linking a user and an event.

Function Descriptions
(Here, briefly describe the functions already explained under queries.py and commands.py.)

Models
User

Fields: id, username, email

Event

Fields: id, title, event_date, organizer_id

Booking

Fields: id, user_id, event_id, booking_time

Technologies Used
Python 3.8+

SQLAlchemy

SQLite (or any SQLAlchemy-compatible DB)

PrettyTable

Alembic (for migrations)

Resources
Markdown Cheat Sheet

PrettyTable Docs

SQLAlchemy Docs

Alembic Docs

Author EDEL  OMONDI

