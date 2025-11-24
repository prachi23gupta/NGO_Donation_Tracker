# main.py - Entry point
from modules.donor_management import add_donor, list_donors
from modules.donation_management import add_donation
from modules.report_generator import total_donations, donations_by_donor, view_all_donations

def main_menu():
    while True:
        print("=== NGO Donation Tracking System ===")
        print("1. Add Donor")
        print("2. List Donors")
        print("3. Add Donation")
        print("4. View All Donations")
        print("5. Total Donations")
        print("6. Donations by Donor")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        print()
        if choice == '1':
            add_donor()
        elif choice == '2':
            list_donors()
        elif choice == '3':
            add_donation()
        elif choice == '4':
            view_all_donations()
        elif choice == '5':
            total_donations()
        elif choice == '6':
            donations_by_donor()
        elif choice == '7':
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice! Please enter 1-7.\n")

if __name__ == "__main__":
    main_menu()
