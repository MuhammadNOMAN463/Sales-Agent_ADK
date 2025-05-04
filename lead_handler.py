"""
Lead Conversation Handler
Manages the complete interaction flow with leads
"""

import session_manager
from utils import save_to_csv, ask_question, send_message
from follow_up_scheduler import follow_up
import time

# Core qualification questions for leads
QUESTIONS = [
    "What is your age?",
    "Which country are you from?",
    "What product or service are you interested in?"
]


def handle_lead(lead):
    """
    Main lead handling workflow

    Args:
        lead (dict): Lead information with 'lead_id' and 'name'
    """
    # Short delay to prevent message overlap in console
    time.sleep(0.2)

    # Initialize session in Firestore
    session = session_manager.create_session(lead["lead_id"], lead["name"])

    # Initial engagement message
    send_message(lead["name"],
                 f"Hey {lead['name']}, thank you for filling out the form. "
                 "I'd like to gather some information from you. Is that okay?")

    # Consent check
    consent = ask_question("Consent (yes/no): ", lead["name"])
    if consent.lower() != "yes":
        send_message(lead["name"], "Alright, no problem. Have a great day!")
        save_to_csv(lead, status="no_response")
        return

    # Question-answer loop
    for question in QUESTIONS:
        response = ask_question(question + " ", lead["name"])
        if not response:
            follow_up(lead)  # Trigger follow-up if no response
            return
        session[question] = response  # Store response in session

    # Finalize lead data
    lead.update({
        "age": session[QUESTIONS[0]],
        "country": session[QUESTIONS[1]],
        "interest": session[QUESTIONS[2]],
        "status": "secured"  # Mark as successfully completed
    })
    save_to_csv(lead)