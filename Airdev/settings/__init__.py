from decouple import config

# you need to set DEBUG = TRUE or False depending on the enviroment. Debug False is for production & True is for Local.

DEBUG = config('DEBUG', default=False, cast=bool)
if DEBUG:
   from .development import *
else:
   from .production import *