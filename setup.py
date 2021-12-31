import pandas as pd
import fastf1 as ff1
import os


def setUpCache(path=""):
    if not os.path.exists(os.path.join(path,"./cache")):
        os.mkdir(os.path.join(path,"./cache"))
    ff1.Cache.enable_cache(os.path.join(path,"./cache")) 


def main():
    setUpCache()



# ##################################################################################################
main()

