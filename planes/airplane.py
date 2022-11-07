class Airplane(object, metaclass=type):  # __init__ jest w object
    def get_num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)
