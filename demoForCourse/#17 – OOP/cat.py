class Cat:
  name = None
  age = None
  isHappy = None

  # Constructor
  def __init__(self, name = None, age = None, isHappy = None):
    self.name = name
    self.age = age
    self.isHappy = isHappy

  def get_data(self):
    print(self.name, "age:", self.age, "isHappy:", self.isHappy)