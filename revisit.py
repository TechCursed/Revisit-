import webbrowser
from time import sleep

url = input('Enter URL to refresh, including "http://: ')

while True:
    print("refreshing...")
    webbrowser.open(url, new=0)
    sleep(5)
