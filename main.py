from simulate_trigger import simulate_form_submission
from lead_handler import handle_lead

def main():
    leads = simulate_form_submission()
    for lead in leads:
        handle_lead(lead)

if __name__ == "__main__":
    main()

    # Create thread per lead
    for lead in leads:
        thread = threading.Thread(target=handle_lead, args=(lead,))
        threads.append(thread)
        thread.start()

    # Wait for completion
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()