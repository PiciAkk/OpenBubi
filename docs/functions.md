# Bult-in functions

## `BubiUser`
- `info()` - returns information in JSON (not dictionary) format -> if you want it in dictionary format, `import json`, and use `json.loads(info())`
- `getScreenName()` - grabs the screen name from `info()`, and returns it
- `getLoginKey()` - grabs the login key from `info()`, and returns it
- `callOtherEndpoint(relativeURL, data)` (*relativeURL needs to be a string, and data needs to be a dictionary*) - calls the specified `endpoint` with the specified `data` (plus `loginkey`, `domain`, `apikey`, `show_errors`), and returns the output
- `rentBike(bikeNumber)` (*bikeNumber needs to be a string*) - rents a bike, and returns the output
- `getActiveRentals()` - returns active rentals
