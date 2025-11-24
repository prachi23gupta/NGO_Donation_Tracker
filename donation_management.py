# donation_management.py - Functions to record donations
from models import Donation
from database import save_donation, load_donors

def add_donation():
    donors = load_donors()
    if not donors:
        print("No donors found. Please add a donor first.\n")
        return
    print("Select donor to donate:")
    for idx, donor in enumerate(donors, start=1):
        print(f"{idx}. {donor.name}")
    while True:
        try:
            choice = int(input("Enter donor number: "))
            if choice < 1 or choice > len(donors):
                print("Invalid choice.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")
    donor_name = donors[choice-1].name
    while True:
        try:
            amount = float(input(f"Enter donation amount for {donor_name}: "))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")
    donation = Donation(donor_name, amount)
    save_donation(donation)
    print(f"Donation of ₹{amount} recorded from {donor_name}.\n")