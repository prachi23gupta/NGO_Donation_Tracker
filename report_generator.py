# report_generator.py - Generate reports
from database import load_donations

def total_donations():
    donations = load_donations()
    total = sum(d.amount for d in donations)
    print(f"Total Donations Collected: ₹{total}\n")

def donations_by_donor():
    donations = load_donations()
    name = input("Enter donor name to view donations: ")
    donor_donations = [d.amount for d in donations if d.donor_name.lower() == name.lower()]
    if donor_donations:
        print(f"{name} donated a total of ₹{sum(donor_donations)} in {len(donor_donations)} donation(s).\n")
    else:
        print(f"No donations found for {name}.\n")

def view_all_donations():
    donations = load_donations()
    if not donations:
        print("No donations yet.\n")
        return
    print("All Donations:")
    for idx, d in enumerate(donations, start=1):
        print(f"{idx}. {d.donor_name} donated ₹{d.amount}")
    print()