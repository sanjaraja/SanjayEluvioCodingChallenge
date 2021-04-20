from concurrent.futures import ThreadPoolExecutor
import requests

id_set = set()
def fetch(session, url, id):
    if id not in id_set:
        id_set.add(id)
        print("Entering fetch")
        headers = {
            "Authorization": "Y1JGMmR2RFpRc211MzdXR2dLNk1UY0w3WGpI"
        }
        url = url + id
        with session.get(url, headers=headers) as response:
            print(response.status_code) #Printing the response status code. 
    else:
        print("This is a duplicate ID")

if  __name__ == "__main__":
    ids = ["cRF2dvDZQsmu37WGgK6MTcL7XjH"]
    for num in range(0, 19): #Edit the range if you want more IDS
        ids.append(str(num))

    url = "https://eluv.io/items/"
    with ThreadPoolExecutor(max_workers=5) as executor: #Ensuring that there are only 5 threads at a time to avoid too many requests rerror
        with requests.Session() as session:
            executor.map(fetch, [session] * 20, [url] * 20, ids) #Change the 20 here if you want more IDs
            executor.shutdown(wait=True)
