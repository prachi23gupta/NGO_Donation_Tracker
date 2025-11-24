# donor_management.py - Functions to manage donors
from models import Donor
from database import save_donor, load_donors

def add_donor():
    name = input("Enter donor's name: ")
    if name.strip() == "":
        print("Name cannot be empty!\n")
        return
    if any(d.name.lower() == name.lower() for d in load_donors()):
        print(f"{name} is already a donor.\n")
        return
    donor = Donor(name)
    save_donor(donor)
    print(f"Donor '{name}' added successfully!\n")

def list_donors():
    donors = load_donors()
    if not donors:
        print("No donors yet.\n")
        return
    print("Donor List:")
    for idx, donor in enumerate(donors, start=1):
        print(f"{idx}. {donor.name}")
    print()