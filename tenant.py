class Tenant: #import  file to main rental.py
    def __init__(self, name, house_number, rent, paid=False):
        self.name = name
        self.house_number = house_number
        self.rent = rent
        self.paid = paid
