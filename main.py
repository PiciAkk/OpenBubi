import openbubi

map = openbubi.BubiMap("bkk")
user = openbubi.BubiUser("+36307339120", "314974")

print(map.getNearestStationByAddress("Váci utca"))

# print(map.listAllStations())
# print(map.getNearestStationByAddress("Hungary, Budapest, Móricz Zsigmond körtér"))
# print("Current login key is " + user.getLoginKey())
# print(MarciUser.info())
# print(BudapestMap.getNearestStation(100, 100))
