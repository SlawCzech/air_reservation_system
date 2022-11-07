from planes import Airplane


class AirbusA380(Airplane):
    @staticmethod  # Nie potrzebuje obiektu, żeby ją wywołać
    def get_name():
        return 'AirbusA380'

    @staticmethod
    def seating_plan():
        return range(1, 51), 'ABCDEGHJK'
