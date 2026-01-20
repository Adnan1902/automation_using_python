#ticket_classifier.py

#Define ticket categories and keywords
CATEGORIES = {
    "Authentication": ["login", "password", "unauthorized", "access denied"],
    "Application": ["crash", "exception", "500", "error"],
    "Network": ["timeout", "latency", "dns", "network"],
    "Database": ["database", "db", "query", "connection refused"],
    "Hardware": ["cpu", "memory", "disk", "server"]
}

TICKETS_FILE = "sample_tickets.txt"

def classify_ticket(ticket):
    ticket_lower = ticket.lower()

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in ticket_lower:
                return category


    return "Other"

def main():
    print("Ticket Categorization Results:\n")

    with open(TICKETS_FILE, "r") as file:
        for line in file:
            ticket = line.strip()
            if ticket:
                category = classify_ticket(ticket)
                print(f"Ticket: {ticket}")
                print(f"Category: {category}")
                print("-" * 50)

if __name__ == "__main__":
    main()