from animal import Animal

class Sheep(Animal):
  pass
  sound = 'Baah'

  def noise(self):
      self.sound.upper()