class Person():
  id = None
  localization = None
  checked = false

  def __init__(self, id):
    self.id = id
  
  def update_localization(self, localization):
    self.localization = localization
