from systemadmin import SystemAdmin
from trainer import Trainer
import database
import datetime

class SuperAdmin(SystemAdmin):

  def __init__(self, username, password, firstName = "", lastName = "", registrationDate = datetime.datetime.now()):
    super().__init__(username, password, firstName, lastName, registrationDate)
    self.role = "superadmin"
  
  def check_users():
    # List all trainers, systemadmins in the system and their role.
    trainers : list[Trainer] = database.database.get_all_trainers() or list()
    systemadmins : list[SystemAdmin] = database.database.get_all_systemadmins() or list()
    for trainer in trainers:
      print(f"Trainer: {trainer[1]} - {trainer[3]}")
    for systemadmin in systemadmins:
      print(f"SystemAdmin: {systemadmin[1], systemadmin[6]}")
    input("Press enter to continue...")