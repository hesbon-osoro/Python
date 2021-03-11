import random
import time
import webbrowser
import sys

while True:
    sites = random.choice(['google.com','facebook.com','youtube.com'])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randint(2,5)
    time.sleep(seconds)
    sys.exit()