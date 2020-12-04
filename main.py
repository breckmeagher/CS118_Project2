"""
    Evaluates the forecast for the route with warmest average temperature and finds
    the combination of hotels that max out a hotel budget.
"""
__author__ = "Breck Meagher"
__email__ = "meagherb@my.erau.edu"
__version__ = "1.0"

from itertools import permutations, combinations_with_replacement

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}


HOTEL_BUDGET = 850
STOPS = 5


def avg_temp(t):
    """
    Finds the average of a list of temperatures.
    """
    avg = sum(t) / len(t)
    return avg


def cost(t):
    """
    Finds the cost of a specific list of hotel combinations.
    """
    prices = sum([hotel_rates[i] for i in t])
    return prices


if __name__ == "__main__":
    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())

    routes = list(permutations(cities, STOPS))
    forecasts = [[city_temps[city][i] for city, i in zip(routes[k], list(range(STOPS)))] for k in range(len(routes))]
    warmest = max(forecasts, key=avg_temp)
    the_route = ' => '.join(map(str, routes[forecasts.index(warmest)]))
    # The forecasts line creates a list of lists of temperatures for each permutation. Due to the fact
    # that accessing specific temperatures requires a few layers of iteration, the temperatures are
    # tied back to the permutation (list of cities), using the index function.

    plans = list(combinations_with_replacement(hotels, STOPS))
    best = min(plans, key=lambda t: HOTEL_BUDGET - cost(t) if HOTEL_BUDGET >= cost(t) else HOTEL_BUDGET)
    formatted = ', '.join(map(str, best))
    # Order is not important when it comes to hotels and it is possible to stay at the same hotel more
    # than once, so combinations with replacement was the method to choose. The best combination is
    # found by evaluating each combination that is within the budget for its proximity to the budget.

    print(f'FINDING THE BEST ROUTE AND HOTELS ALONG THE WAY \n\n'
          f'Here is your best route: {the_route} \n The average of the daily max temp. is {avg_temp(warmest)}F \n\n'
          f'To max out your hotel budget, stay at these hotels: {formatted}, '
          f'totaling ${cost(best)}')
