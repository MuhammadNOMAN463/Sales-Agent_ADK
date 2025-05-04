"""
Utility Functions
Handles I/O operations with thread safety
"""

import csv
import os
import threading

# Thread locks for resource synchronization
csv_lock = threading.Lock()  # Protects CSV write operations
input_lock = threading.Lock()  # Ensures sequential user input


def send_message(name, msg):
    """Simulates sending a message to a user through console output"""
    print(f"[Bot to {name}]: {msg}")


def ask_question(prompt, lead_name=None):
    """
    Gets user input with lead-specific context

    Args:
        prompt (str): Question to display
        lead_name (str, optional): Lead identifier for context

    Returns:
        str: User's response
    """
    identifier = f"[{lead_name}] " if lead_name else ""
    with input_lock:  # Ensures only one question is asked at a time
        return input(f"{identifier}{prompt}")


def save_to_csv(data, status=None):
    """
    Appends lead data to CSV file with thread-safe operations

    Args:
        data (dict): Lead information
        status (str, optional): Override status value
    """
    data["status"] = status or data.get("status", "pending")
    with csv_lock:  # Ensures atomic CSV operations
        file_exists = os.path.isfile("leads.csv")
        with open("leads.csv", mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["lead_id", "name", "age", "country", "interest", "status"])
            if not file_exists:
                writer.writeheader()  # Write header only for new files
            writer.writerow(data)