# database.py - In-memory "database"

DONORS_DB = []     # List of donors
DONATIONS_DB = []  # List of donations

def save_donor(donor):
    DONORS_DB.append(donor)

def save_donation(donation):
    DONATIONS_DB.append(donation)

def load_donors():
    return DONORS_DB

def load_donations():
    return DONATIONS_DB