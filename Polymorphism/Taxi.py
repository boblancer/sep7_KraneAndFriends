from Polymorphism.incomplete_code import Transportation

class Taxi(Transportation):
   def __init(self, start, end, distance):
      Transportation.__init__(self, start, end, distance)

   def find_cost(self):
      return self.distance * 50