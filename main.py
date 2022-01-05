import pandas as pd
import fastf1 as ff1
from requests.sessions import session
import tools_library as tl
import ff1_tools_library as ff1tl
import os



# ##################################################################################################
cache_path = ff1tl.setUpCache(
            path="/mnt/e01887ec-e5a8-4f27-aa3e-708f361b870a/formula1_analytics_db"
            )
print(cache_path)
ff1tl.extractWeekend(2021, 1)