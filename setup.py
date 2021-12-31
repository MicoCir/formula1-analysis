import pandas as pd
import fastf1 as ff1
import os


def setUpCache(path=""):
    if not os.path.exists(os.path.join(path,"./cache")):
        os.mkdir(os.path.join(path,"./cache"))
    ff1.Cache.enable_cache(os.path.join(path,"./cache")) 


def main():
    setUpCache()
    istambul_quali = ff1.get_session(2021, 'Turkey', 'Q')
    laps = istambul_quali.load_laps(with_telemetry=True)
    laps.to_csv("istambul_quali.csv")



# ##################################################################################################
main()

