import random

class RandomGen:

    def __init__(self, driver):
        self.driver = driver

    def valid_gen(self, search):
        r = random.randint(0 , len(search) -1)
        search_term = search[r]
        self.driver.find_element_by_id("search_query_top").send_keys(search_term)

    def invalid_gen(self, invalid_search):
        r = random.randint(0, len(invalid_search) - 1)
        search_term = invalid_search[r]
        self.driver.find_element_by_id("search_query_top").send_keys(search_term)