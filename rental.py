from tenant import Tenant  

def main():
    print("Welcome to Kibathi Rental Management System")
    tenants = [] # list to store tenant objects in memory, this allows us to manage tenant data during the program's execution without needing a database or file storage for simplicity

    while True:  # infinite loop
        print("\nMenu:")
        print("1. Add tenant")
        print("2. View tenants")
        print("3. Record payment")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1': # we  use  if-elif  when they are  more  choices  we use  if-else  when there are  only two choices  
            add_tenant(tenants)
        elif choice == '2':
            view_tenants(tenants)
        elif choice == '3':
            record_payment(tenants)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break #used to break the  program when the user chooses to exit, it prevents the infinite loop from running indefinitely and allows the program to terminate gracefully
        else:
            print("Invalid choice. Please try again.")


def add_tenant(tenants):
    name = input("Enter tenant's name: ")
    house_number = input("Enter tenant's house number: ")
    rent = float(input("Enter tenant's rent amount: "))
    tenant = Tenant(name, house_number, rent)
    tenants.append(tenant)#used to add  newly tenant
    print(f"Tenant {name} added successfully.")


def view_tenants(tenants):
    if not tenants:
        print("No tenants found.")
        return

    print("\nList of Tenants:")
    for t in tenants:
        status = "Paid" if t.paid else "Not Paid"
        print(f"Name: {t.name}, House: {t.house_number}, Rent: {t.rent}, Status: {status}")


def record_payment(tenants):
    if not tenants: 
        print("No tenants found!")
        return

    name = input("Enter tenant name to record payment: ").strip() #strip method  used to remove spaces from begining and the end of a string

    found = False
    for t in tenants:
        if t.name.lower() == name.lower():
            t.paid = True
            print(f"Payment recorded for {t.name}")
            found = True
            break

    if not found:
        print("Tenant not found!")


if __name__ == "__main__":
    main()