### Get an API key from https://e621.net/users/home
username = "USERNAME HERE"
api_key = "API KEY HERE"
###

import argparse
import requests
import base64

max = 4300000
id_length = 6

def is_valid_id(id):
    if id > max: return 0
    if len(str(id)) != id_length: return 0
    
    return 1

def get_id_from_snowflake(snowflake):
    ids = []
    offset = 0
    flake_len = len(snowflake)
    start_pos = flake_len - id_length
    
    while offset <= start_pos:
        id = snowflake[start_pos-offset:flake_len-offset]
        if is_valid_id(int(id)):
            ids.append(id)
         
        offset += 1
    
    return ids

def find_e621_posts_from_ids(ids, limit):
    valid_ids = {}
    
    headers = {
        "User-Agent": "Snowflake2E621/1.0.0",
        "Authentication": "Basic "+str(base64.b64encode(bytes(username+":"+api_key, 'utf-8')))
    }
    
    for id in ids:
        if len(valid_ids) >= limit: break
        url = "https://e621.net/posts/"+id
        
        r = requests.get(url+".json", headers=headers)
        
        if r.status_code != 200: continue
        
        r = r.json()

        if r["post"]["flags"]["deleted"] == True: continue
        
        valid_ids[url] = r["post"]
        
    return valid_ids

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("snowflake")
    parser.add_argument("amount")

    args = parser.parse_args()

    ids = get_id_from_snowflake(args.snowflake)
    posts = find_e621_posts_from_ids(ids, int(args.amount))

    for post in posts:
        data = posts[post]
        print(post, "| Score:", data["score"]["total"], "| Rating:", data["rating"], "| Favorites:", data["fav_count"])
