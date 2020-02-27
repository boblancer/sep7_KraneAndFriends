import transportation
class Train( Transportation ):

   def __init__( self, start, end, distance ,numberOfStations):
      Transportation.__init__( self, start, end, distance)
      self.numberOfStations = numberOfStations

   def find_cost( self ):
      return 5 * self.numberOfStations
