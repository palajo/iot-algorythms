class Hamster:

    def __init__(self, norm, greed):
        self.norm = norm
        self.greed = greed

    def __str__(self):
        return "{} {}".format(self.norm, self.greed)