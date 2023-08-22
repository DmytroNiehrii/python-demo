class Building:
  year = None
  city = None

  def __init__(self, year, city):
    self.year = year
    self.city = city

  def get_info(self):
    print("Year:", self.year, ". City:", self.city)

class School(Building):
  pupils = 0

  def __init__(self, pupils, year, city):
    super(School, self).__init__(year, city)
    self.pupils = pupils

  # Override
  def get_info(self):
    super().get_info()
    print("Pupils:", self.pupils)

school = School(10, year=2000, city='Moscow')
school.get_info()