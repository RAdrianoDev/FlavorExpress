from models.restaurant import Restaurant


restaurant_brazil = Restaurant('brazilian Food', 'Brazilian')
restaurant_brazil.add_evaluation('John', 5)
restaurant_brazil.add_evaluation('Mary', 4)
restaurant_brazil.add_evaluation('Peter', 4.5)
restaurant_italy = Restaurant('italian Food', 'Italian')
restaurant_japan = Restaurant('japanese Food', 'Japanese')
restaurant_mexico = Restaurant('mExIcan food', 'Mexican')
restaurant_china = Restaurant('Chinese Food', 'Chinese')
restaurant_india = Restaurant('Indian Food', 'Indian')
restaurant_france = Restaurant('French Food', 'French')
restaurant_usa = Restaurant('American Food', 'American')
restaurant_korea = Restaurant('Korean Food', 'Korean')
restaurant_brazil.activate()
restaurant_japan.activate()
restaurant_korea.activate()
restaurant_china.activate()


def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()
