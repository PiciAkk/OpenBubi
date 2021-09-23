import openbubi
import requests

output = requests.post("https://api-budapest.nextbike.net/api/rent.json",
data={
"apikey": "Bbx3nGP291xEtDmq",
"show_errors": 1,
"loginkey": openbubi.BubiUser("+36307339120", "314974").getLoginKey(),
"bike": "860680"
}).text
print(output)
