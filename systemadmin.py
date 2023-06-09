from trainer import Trainer
from datetime import datetime

class SystemAdmin(Trainer):
  def __init__(self, username, password, firstName, lastName, registrationDate = datetime.now()):
    super().__init__(username, password, firstName, lastName, registrationDate)