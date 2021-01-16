import requests, json
import datetime as dt

with open("../cred.json") as f:
    cred=json.loads(f.read())
token = cred['pixela']['token']
username = f"{cred['pixela']['username']}"

base_npt = f"{cred['pixela']['base_endpoint']}"

now = dt.datetime.now()
format_now = now.strftime("%Y%m%d")

# Create user

parameters = {
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

crt_user_npt = "https://pixe.la/v1/users"

response = requests.post(url=crt_user_npt,json=parameters)
response.raise_for_status()
print(response.text)

# Create graph

crt_grph_npt = f"{base_npt}/v1/users/{username}/graphs"
grph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN":token
}
response = requests.post(url=crt_grph_npt,json=grph_config,headers=headers)
print(response.text)

# https://pixe.la/v1/users/tduong10101/graphs/graph1.html
update_grp = f"{base_npt}/v1/users/{username}/graphs/graph1"
grph_config = {
    "timezone":"Australia/Melbourne"
}
headers = {
    "X-USER-TOKEN":token
}
response = requests.put(url=update_grp,json=grph_config,headers=headers)
print(response.text)

crt_pixel_npt = f"{base_npt}/v1/users/{username}/graphs/graph1"


print(format_now)
post_config = {
    "date":format_now,
    "quantity":"1"
}

headers = {
    "X-USER-TOKEN":token
}

response = requests.post(url=crt_pixel_npt,json=post_config,headers=headers)
print(response.text)

update_pxl = f"{base_npt}/v1/users/{username}/graphs/graph1/{format_now}"

put_config = {
    "quantity":"2"
}
headers = {
    "X-USER-TOKEN":token
}
response = requests.put(url=update_pxl,json=put_config,headers=headers)
print(response.text)

delete_pxl = f"{base_npt}/v1/users/{username}/graphs/graph1/20210116"
headers = {
    "X-USER-TOKEN":token
}
response = requests.delete(url=delete_pxl,headers=headers)
print(response.text)