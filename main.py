from riotwatcher import LolWatcher
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('RIOT_API')
watcher = LolWatcher(API_KEY)

free_champs = watcher.champion

print(free_champs.rotations)