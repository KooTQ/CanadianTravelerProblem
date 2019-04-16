
class Connection:
    def __init__(self, end_cell, weight, probability, quality):
        self.__end_cell = end_cell
        self.__weight = weight
        self.__probability = probability
        self.quality = quality

    def get_end_cell(self):
        return self.__end_cell

    def get_weight(self):
        return self.__weight

    def get_probability(self):
        return self.__probability


# End of file
