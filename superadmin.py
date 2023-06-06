from systemadmin import SystemAdmin

class SuperAdmin(SystemAdmin):

  def __init__(self, username, options):
    super().__init__(username, options)
  
  pass