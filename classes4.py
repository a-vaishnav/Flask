class Flight():
    
    counter=1
    
    def __init__(self, origin, destination,duration):
        self.id=Flight.counter
        Flight.counter+=1

        self.passengers=[]

        self.origin=origin
        self.destination=destination
        self.duration=duration

    def print_flight(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print('Passengers')
        for passenger in self.passengers:
            print(passenger)

    def add_passenger(self, p):
        self.passengers.append(p.name)
        p.flight_id= self.id


class Passenger():
    def __init__(self,name):
        self.name=name

def main():

    f= Flight('New York', 'Dubai',450)

    alice=Passenger('Alice')
    bob=Passenger('Bob')

    f.add_passenger(alice)
    f.add_passenger(bob)

    f.print_flight()

if __name__ == "__main__":
    main()
