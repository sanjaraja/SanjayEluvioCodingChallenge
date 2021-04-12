from concurrent.futures import ThreadPoolExecutor
import requests

def fetch(session, url, id):
    print("Entering fetch")
    headers = {
        "Authorization": "Y1JGMmR2RFpRc211MzdXR2dLNk1UY0w3WGpI"
    }
    url = url + id
    print(url)
    with session.get(url, headers=headers) as response:
        print(response.status_code)

if  __name__ == "__main__":
    ids = ["cRF2dvDZQsmu37WGgK6MTcL7XjH"]
    for num in range(0, 20):
        ids.append(str(num))

    url = "https://eluv.io/items/"
    with ThreadPoolExecutor(max_workers=5) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * 20, [url] * 20, ids)
            executor.shutdown(wait=True)