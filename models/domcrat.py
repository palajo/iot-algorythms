class Domcart:
    def __init__(self, max_weight, producer, color, weight):
        self.max_weight = max_weight
        self.producer = producer
        self.color = color
        self.weight = weight

    def __str__(self):
        return "\nMax weight: {} \nProducer: {} \nColor: {} \nWeight: {}\n".format(self.max_weight, self.producer, self.color, self.weight)
         