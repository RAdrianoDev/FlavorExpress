from models.evaluation import Evaluation

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._evaluation = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self._name} - {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f'{"*** Restaurant Name ***".ljust(25)} | {"*** Restaurant Category ***".ljust(25)} | {"*** Rating ***".ljust(25)} | *** Restaurant Active ***')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.average_rating).ljust(25)} | Active: {restaurant.active}')

    @property
    def active(self):
        return '☒' if self._active else '☐'
    
    def activate(self):
        self._active = not self._active
    
    def add_evaluation(self, customer, rating):
        if 0 < rating <= 5:
            evaluation = Evaluation(customer, rating)
            self._evaluation.append(evaluation)

    @property
    def average_rating(self):
        return round(sum([evaluation.rating for evaluation in self._evaluation]) / len(self._evaluation), 1) if self._evaluation else ' - '