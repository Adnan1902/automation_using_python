#Task 3: Automated TIcket Categorization

## Overview
This task implements a rule-based automation script to automatically categorize incoming support tickets based on keywords present in the ticket description.

The objective is to reduce manual effort in ticket triaging and improve routing efficiency in support/helpdesk systems.

---

## Problem Statement
Support teams recieve a high volume of tickets daily. Manually categorizing each ticket slows down response time and can lead to incorrect routing.

This automation categorizes tickets instantly using predefined rules.

---

## SOlution Approach
- Read ticket descriptions from a text file
- Define categories with associated keywords
- Match ticket content against keywords
- Assign the most relevant category
- Default to **other** if no match is found

---

### Categories Implemented 
- Authentication (login, password, unauthorized, access)
- Application (error, crash, exception, 500)
- Network (timeout, latency, DNS, network)
- Database (DB, query, connection refused)
- Hardware (CPU, memory, disk, server)
- Other (no match)

---

## Project Structure
task3-ticket-categorization/
|---ticket_classifier.py
|---sample-tickets.txt
|---README.md
|---.gitignore

