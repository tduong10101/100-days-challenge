from art import logo
import os
print(logo)
print("Welcome to thge secret auction program.")
another_bid = ""
bids = []
def addBid (name, bidAmount):
    bids.append({
        "name": name,
        "bidAmount": bidAmount
    })

while another_bid != "no":
    another_bid = ""
    name = input("What is your name?: ")
    bidAmount = int(input("What's your bid?: $"))
    addBid(name, bidAmount)
    while not (another_bid == "yes" or another_bid == "no"):
        another_bid = input("Are there any other bidders? Type 'yes' or 'no': ")
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 
maxbid = [{"bidAmount": 0}]
for bid in bids:
    if bid["bidAmount"] > maxbid[0]["bidAmount"]:
        maxbid = [bid]
    elif bid["bidAmount"] == maxbid[0]["bidAmount"]:
        maxbid.append(bid)


if len(maxbid) == 1:
    namestxt = maxbid[0]["name"]
else:
    names = []
    for bid in maxbid:
        names.append(bid["name"])
    namestxt = ", ".join(names)

print (f"The winner is {namestxt} with bid of ${maxbid[0]['bidAmount']}")