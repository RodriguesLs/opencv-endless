class Person():
  id = None
  init_location = None
  localization = None
  checked = False
  last_localization = []

  def __init__(self, id, locale):
    self.id = id
    self.init_location = locale
  
  def update_localization(self, localization):
    self.localization = localization
    self.last_localization.append(localization)
    
  # def save_localalization(self, localization):