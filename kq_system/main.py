"""
SOME QUESTION
"""
class Flight:
    def __init__(self,name,route):
        self.name=name
        self.route=route
        self.price=None
        self.seats=None
        self.rating=None
     
class AirlineSystem:
    def __init__(self):
        self.flight_routes=[]
        
        self.unique_destinations=set()
        self.popular_routes=[]
        self.expensive_routes=[]
        self.few_seats=[]
    def set_flight_routes(self):
        
        i=1
        while True:
            print("...Type 'quit' to quit (at any point) from adding more routes/flights...")  
            while True:          
                    flight_number=input(f"enter flight number for number {i} > ")
                    if flight_number!="" :
                        break
                    else:
                        print(f"error:")
                        print("reenter the flight number as a non empty string")
                        
            while True:
                
                flight_route=input(f"Enter flight number {flight_number}'s route > ")
                if flight_route!="":
                    break
                else:
                    print(f"error: ")
                    print("reenter the flight number as a non empty string")
            if flight_route =="quit" or flight_number=="quit":
                if len(self.flight_routes)<10:
                    print("You cant quit yet the length of flight routes is less than 10")                   
                    continue
                else:
                    print("successfully quit")
                    break
            self.flight_routes.append(Flight(flight_number,flight_route))
            
            i+=1
        return self.flight_routes
    
    def set_price(self):
        for flight in self.flight_routes:      
            flight.price=int(input("Please enter the price for {flight.name} > "))
        print("You are done inputing all the flight prices")     
    def set_seats(self):
        for flight in self.flight_routes:    
            flight.seats=int(input("Please enter the number of seats available for {flight.name} > "))
        print("You are done inputing all the flight available seats")  
    def set_ratings(self):
        for flight in self.flight_routes:      
            flight.rating=float(input("Please enter the ratings for {flight.name} > "))
        print("You are done inputing all the flight ratings")  
    def set_unique_destinations(self):
        for flight in self.flight_routes:
            temp_routes=flight.route.strip().split(" to ")
            if temp_routes[1] not in self.unique_destinations:
                self.unique_destinations.add(temp_routes[1])
        self.get_everything() 
    def get_everything(self):
        for flight in self.flight_routes:
            print(f"The flight {flight.name} costs {flight.price} ,has {flight.seats} seats and {flight.rating} ratings")
    def set_popular_routes(self):
        for flight in self.flight_routes:
            if flight.rating>3:
                self.popular_routes.append(flight)
    def set_expensive_routes(self):
        for flight in self.flight_routes:
            if flight.price>500:
                self.expensive_routes.append(flight)
    def set_few_seats(self):
        for flight in self.flight_routes:
            if flight.seats<10:
                self.popular_routes.append(flight)  
    def get_everything_after(self):
        print("the popular routes are...")
        for flight in self.popular_routes:
            print(flight.name,flight.rating)
        print("the expensive routes are ...")
        for flight in self.expensive_routes:
            print(flight.name,flight.price)
        print("the few seated air planes are")
        for flight in self.few_seats:
            print(flight.name,flight.seats)
    
def main():
    airline=AirlineSystem()
    airline.set_flight_routes()
    airline.set_price()
    airline.set_ratings()
    airline.set_seats()
    airline.set_unique_destinations()
    airline.get_everything()
    airline.set_popular_routes()
    airline.set_expensive_routes()
    airline.set_few_seats()
    airline.get_everything_after()

 

main()   
