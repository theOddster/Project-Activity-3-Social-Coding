
"""
    "Eto yung  function na ilalagay"
    1. Route Type = (Done) - Kevin
    2. Gas Price for (PH) - Jeric (DONE)
    3. Has Ferry - Joey (Done)
    4. Bounding Box - Chloe
    5. Use Traffic = Gawing aware yung user na hindi traffic based yung system - Jeric (DONE)
"""
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "rKYdRUvO2kk0NiNjlQnZ5r9Hm0dALE3f"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if orig == "quit" or orig == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")

        if json_data["route"]["options"]["useTraffic"] == False:
            print("**********************************************")
            print("Not accurate traffic info.")
            print("**********************************************\n")
        else:
            print("**********************************************")
            print("Accurate traffic info.")
            print("**********************************************\n")

        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " +
              str("{:.2f}".format((json_data["route"]["distance"]) * 1.61)))
        print("Fuel Used (Ltr): " +
              str("{:.2f}".format((json_data["route"]["fuelUsed"]) * 3.78)))
        print("Diesel total price: " +
              str("{:.2f}".format((json_data["route"]["fuelUsed"]) * 3.78 * 71.700)) + "php")

        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"]) * 1.61) + " km)"))
        print("=============================================")
        print("Route type: " + json_data['route']['options']['routeType'])
        print("=============================================")
        print("Need Ferry: " + str(json_data['route']['hasFerry']))
        print("=============================================")
        print("END OF ANALYSIS\n")

    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
