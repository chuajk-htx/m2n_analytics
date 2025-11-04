import tkinter as tk
from tkinter import simpledialog
from sqlalchemy import create_engine

def get_database_connection():
    """Prompt user for database password and establish a connection."""
    # Initialize Tkinter root (doesn't need to be displayed)
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Ask user for their password for MariaDB
    DB_PASSWORD = simpledialog.askstring("Database Login", "Enter your database password:", show='*')
    
    if not DB_PASSWORD:
        raise Exception("No password provided. Please enter a valid password.")
    
    # Database details
    DB_USER = 'root'
    DB_HOST = '127.0.0.1'
    DB_PORT = '3306'
    DB_NAME = 'inspectorate_implementation'

    connection_string = f'mariadb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    
    return create_engine(connection_string)

# Example usage:
engine = get_database_connection()