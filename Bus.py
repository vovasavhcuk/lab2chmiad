class Bus:
    count = 0
    name = str()
    numSeats = int()
    number = int()

    def __init__(self):
        Bus.count +=1
        print("count =", Bus.count)

    def __init__(self, name, numSeats, number):
        Bus.count += 1
        print("count =", Bus.count)
        try:
            self.name = str(name)
            self.numSeats = int(numSeats)
            self.number = int(number)
        except ValueError as e:
            print(e)

    def set_name(self, nm):
        self.name = nm

    def set_numSeats(self, ns):
        self.numSeats = ns

    def set_number(self, number):
        self.number = number;

    def get_name(self):
        return self.name;

    def get_numSeats(self):
        return self.numSeats;

    def get_number(self):
        return  self.number;

    def show(self):
        print("Name - ", self.name, "\nNumSeats - ", self.numSeats, "\nNumber - ", self.number);
