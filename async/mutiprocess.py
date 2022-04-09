import requests
import multiprocessing
import time


session  = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    try:
        response = session.get(url)
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")
    except Exception as err:
       print("request failed")

def download_all_sites(sites):
    try:
        process_pool = multiprocessing.Pool(initializer=set_global_session) # process initlization params
        process_pool.map(download_site, sites) #procesess bulk execution
    except Exception as err:
        print("mutiprocess failed")
        
if __name__ == "__main__":

    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites) # executing pararell procesess    
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")