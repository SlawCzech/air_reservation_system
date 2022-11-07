from planes import Airplane


class Boeing737Max(Airplane):
    @staticmethod  # Nie potrzebuje obiektu, żeby ją wywołać
    def get_name():
        return 'Boeing737Max'

    @staticmethod
    def seating_plan():
        return range(1, 26), 'ABCDEG'
