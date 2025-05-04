
f"""
Follow-Up Mechanism
Handles delayed follow-up messages for unresponsive leads
"""

import time
from utils import send_message

def follow_up(lead):
    """
    Triggers follow-up message after simulated delay

    Args:
        lead (dict): Lead information for follow-up
    """
    print("⏳ Waiting 24h (simulated)...")
    time.sleep(3)  # Simulated 24h delay (shortened for testing)
    send_message(lead["name"],
                "Just checking in to see if you're still interested. "
                "Let me know when you're ready to continue.")