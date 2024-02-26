from urllib.request import urlopen
import time

def get_load_time(url):
    if ("https" or "http") in url:
        open_this_url = urlopen(url)
    else:
        open_this_url = urlopen("https://" + url)
        
    start = time.time()
    open_this_url.read()
    end = time.time()
    open_this_url.close()
    
    loading_time = end - start
    
    return loading_time


if __name__ == "__main__":
    print("Check load time.")
    url = input("Enter url: ")
    print(f"\n Loading time {url} is {get_load_time(url):.2} seconds.")