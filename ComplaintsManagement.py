import json
import os
from datetime import datetime

complaints_file = "complaints.json"

class Col:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def writepargraph():
    paragraph = ""
    print(Col.BLUE+"Write your Complaint , to stop writing write 'exit' "+Col.RESET)
    while True:
        line = input("")
        if line.lower() == 'exit':
            return paragraph
        paragraph += line + '\n'

def load_complaints():
    if os.path.exists(complaints_file):
        with open(complaints_file, 'r') as file:
            return json.load(file)
    else:
        return []


def save_complaints(complaints):
    with open(complaints_file, 'w') as file:
        json.dump(complaints, file, indent=2)


def submit_complaint(name, email, message,id):
    complaints = load_complaints()
    complaint = {
        "name": name,
        "email": email,
        "message": message,
        "timestamp": str(datetime.now()),
        "StudentID": id
    }
    complaints.append(complaint)
    save_complaints(complaints)
    print(Col.GREEN+"Complaint submitted successfully"+Col.RESET)


def view_complaints():
    complaints = load_complaints()
    if not complaints:
        print(Col.BLUE+"\nNo complaints found.\n"+Col.RESET)
    else:
        for index, complaint in enumerate(complaints, 1):
            print(Col.BLUE+f"\nComplaint #{index}"+Col.RESET)
            print(Col.BLUE+f"Name: {complaint['name']}"+Col.RESET)
            print(Col.BLUE+f"Email: {complaint['email']}\n"+Col.RESET)
            print(Col.BLUE+f"Message: {complaint['message']}"+Col.RESET)
            print(Col.BLUE+f"Timestamp: {complaint['timestamp']}"+Col.RESET)
            print(Col.BLUE+f"Student ID: {complaint['StudentID']}\n"+Col.RESET)


def remove_complaint(index):
    complaints = load_complaints()

    if 1 <= index <= len(complaints):
        removed_complaint = complaints.pop(index - 1)
        save_complaints(complaints)
        print(Col.GREEN+f"Complaint #{index} removed successfully"+Col.RESET)
    else:
        print(Col.RED+"Invalid complaint index"+Col.RESET)


# Example usage:
"""
while True:
    print("\n1. Submit Complaint")
    print("2. View Complaints")
    print("3. Remove Complaint")
    print("4. Exit")

    choice = input("Choose your Choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        message = writepargraph()
        submit_complaint(name, email, message, result[0].getid())

    elif choice == '2':
        view_complaints()

    elif choice == '3':
        index = int(input("Enter the complaint number to remove: "))
        remove_complaint(index)

    elif choice == '4':
        print("Exiting the complaint system. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
"""