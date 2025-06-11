Airline system using Data structures.
You are tasked with developing an online management system for Kenya Airways. This
system will be used by airline administrators to manage flight bookings.
Develop a Python program with the following features:
1. Implement a function that allows the airline admin to enter flight routes. You can
use any of the data structures (lists, dictionaries, tuples). The function should
continue to accept input until the user enters 'quit'. The data structure should
contain at least 10 items. If the user enters less than 10 items, the function should
prompt the user to enter more items until there are at least 10 items in the data
structure.
Example: In this example, we have a list where each item is a tuple containing the flight
number and its route. For instance: ‘flight_routes = [('AA101', 'New York to London'),
('AA102', 'London to New York'), ('AA103', 'New York to Paris')] ‘.
2. Using the `flight_routes` data structure from step 1 and using input from the user,
create a data structure that contains the price of each flight route. For instance:
‘route_price= {'AA101': 500, 'AA102': 450, 'AA103':550}’.
3. Using the `flight_routes` data structure from step 1 and using input from the user,
create another data structure that contains the number of seats available on
each flight. For instance: ‘route_seats= {'AA101': 50, 'AA102': 30, 'AA103':40} ‘.
4. Using the `flight_routes` data structure from step 1 and using input from the user,
create another data structure that records the rating received from passengers
for each flight route. Ratings are scored on a scale from 1 to 5, with 5 indicating
maximum passenger satisfaction. For instance: `route_ratings = {'AA101': 4,
'AA102': 3.5, 'AA103':4.2}.
5. Create a set of all unique destinations available in your flight routes. Use a loop
to iterate over your flight routes and print out each route along with its price,
number of seats, and rating.
6. Finally, create a new function that returns the following separate data structures:
• A data structure named `popular_routes`, which includes routes with a
passenger satisfaction rating of 3 or higher.
• A data structure named `expensive_routes`, which includes routes priced
above $500.
• A data structure named `few_seats`, which includes routes with less than
10 seats available.
• A data structure named `unique_destinations`, which includes all unique
destinations available in your flight routes.