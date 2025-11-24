# models.py - Defines Donor and Donation classes

class Donor:
    def _init_(self, name):
        self.name = name

class Donation:
    def _init_(self, donor_name, amount):
        self.donor_name = donor_name
        self.amount = amount