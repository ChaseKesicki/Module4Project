# The DunnDelivery class demonstrates core OOP concepts:
# - Encapsulation: Data (menu anc prices) and methods are bundled in the class.
# - Abstraction: Complex delivery logic is hedden behind simple method calls.

class DunnDelivery:
    # Constructor method - creates a new instance of a delivery
    def __init__(self):
        # Class attributes demonstrate encapsulation
        # by keeping related data together

        # Menu Attribute - menu of items you can order to be delivered
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuchino", "Peppermint Mocha", "Pumpkin Spice Latte", "Pistachio Latte"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": {"Falafel Wrap", "Hummus & Pita", "Chicken Wrap"}
        }

        # Prices encapsulated within the class
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuchino": 4.99, "Peppermint Mocha": 4.99, "Pumpkin Spice Latte": 4.99, "Pistachio Latte": 4.99,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Falafel Wrap": 8.99, "Hummus & Pita": 7.99, "Chicken Wrap": 8.99          
        }

        # Delivery locations and number of minutes to deliver to that location
        self.delivery_locations = {
            "Library": 10,
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }
    # Show the menu of items available for delivery
    def show_menu(self, category=None):
        if category:
            print(f"\n=== {category} ===")
            # Loop through the items in that specific category on the menu
            # and display them to the user
            for item in self.menu[category]:
                 print(f"{item}: ${self.prices[item]:.2f}")
        else:
            #Show the entire menu
            for category in self.menu: # First show the category name
                 print(f"\n=== {category} ====")
                 # Second show the items within the category
                 for item in self.menu[category]:
                     print(f"{item}: #{self.prices[item]:.2f}")

    # Method to calculate the total cost of the order
    def calculate_total(self, items, has_student_id=False, priority_delivery=False):
        # Calculate the total
        total = sum(self.prices[item] for item in items)

        #Calculate the discount based on the student ID
        if has_student_id and total > 10:
            total *= 0.9
        # If the user wants priority delivey (saves 3 minutes), it costs them an extra 2 dollars
        if priority_delivery:
            total += 2
        # This method returns the total cost of the order to the code that
        # called the method
        return total;

    # Mehtod to calculate the delivery time based on location and time of day
    def estimate_delivery(self, location, current_hour, priority_delivery=False):
        # Calculate the base time
        base_time = self.delivery_locations[location]
        # Subtract 3 minutes if they want priority delivery
        if priority_delivery:
            base_time -= 3

        # Calculate the delivery time based on the time of day (adjust for  busy times of day)
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
             return base_time + 5

        # If they got priority delivery, its 3 minutes faster

        
    
        #If they aren't ordering during a busy time, return the base time with no adjustment
        return base_time

    # Method that prints the orcer (receipt)
    def print_order(self, location, items, current_hour, has_student_id=False, priority_delivery=False):
        # Display the order information
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems Ordered:")
        # Loop through the list of menu items they ordered
        for item in items:
             print(f"- {item}: ${self.prices[item]}:.2f")
    
        # Call the methods to ge tthe total cost and the delivery time
        total = self.calculate_total(items,  has_student_id, priority_delivery)
        delivery_time = self.estimate_delivery(location, current_hour, priority_delivery)

        # Display the subtotal
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")

        # If student payed for priority delivery, display it
        if priority_delivery:
            print("Priority delivery has been applied")

        # Calculate the total with the discount if the student has a student ID

        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student discount applied")

        # display total after discount & estimated delivery time
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")

# Method that lets the user give rating on their delivery
def rate_delivery(rating):
    if 1 <= rating <= 5:
        print(f"Thank you for rating your delivery.  We appreciate your feedback")
    else:
        print("Invalid rating. Please rate between 1 and 5 stars")
        


# main method is executed as soon as the program runs
def main():
    #Create a new delivery object - instanctiating a new object
    delivery = DunnDelivery()

    # Show menu
    delivery.show_menu("Coffee Drinks")

    # Sample order  at 9:30 AM (peak morning hour)
    order = ["Latte", "Bagel"]

    # Display receipt for the order
    delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True, priority_delivery=True);

# Add the line of code to automatically call the main method
if __name__ == "__main__":
    main()