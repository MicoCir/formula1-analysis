import fastf1 as ff1
from requests.sessions import session
import tools_library as tl
import os


# def setUpCache(path=""):
#     if not os.path.exists(os.path.join(path,"cache")):
#         os.mkdir(os.path.join(path,"cache"))
#     ff1.Cache.enable_cache(os.path.join(path,"cache")) 
#     return os.path.join(path,"cache")

def setUpCache(path=""):
    if not os.path.exists(path):
        os.mkdir(path)
    ff1.Cache.enable_cache(path) 
    return os.path.join(path)



def extractWeekend(year, gp):
    possible_events = ["FP1", "FP2", "FP3", "Q", "SQ", "R"]
    for event in possible_events:
        print("\nExtracting:", year, gp, event)
        try:
            sesion = ff1.get_session(year, gp, event)
            sesion.load_laps(with_telemetry=True)
        except:
            print("This", event, "event didn't occur. I continue with the rest.")
