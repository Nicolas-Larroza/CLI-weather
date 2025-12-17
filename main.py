import requests, json, time


class UserIsANaughtyBoy(Exception):
    pass

def main():
    menu = [
    "welcome! please choose what you want to see.",
    "[1] See weather"
        ]
    #i'll add more menu options later, thus im using a list
    for line in menu:
        print(line)
    try:
        selection = input(">")
        if selection == "1":
            print("current or forecast? (1 or 2)")
            request_type = input(">")
            if request_type == "1":
                API_request = "current"
                days = "1"
            elif request_type == "2":
                API_request = "forecast"
                print("how many days shall we forecast? (2 to 14)")
                days = input(">")
            else:
                raise UserIsANaughtyBoy("please comply, thank you")
            time.sleep(0.2)
            print("city?")
            city = input(">")
        else:
            raise UserIsANaughtyBoy("please comply, thank you.")
    except UserIsANaughtyBoy as e:
        print(e)
        exit()
    return city, API_request, days

       
def get_weather(city, API_request, days=1):
    params = {
        "key" : "e16921e57e084bc7873184420251512",
        "q" : city,
        "days" : days
    }
    response = requests.get(f"http://api.weatherapi.com/v1/{API_request}.json", params=params)
    print(response.status_code)


    weather_data = response.json()
    try:
        with open('data.json', 'w') as f:
            json.dump(weather_data, f)
    except KeyError:
        print("something went wrong. perhaps you asked for an invalid city?")
    

if __name__ == '__main__':
    city, API_request, days = main()
    get_weather(city, API_request, days)


    
    
    """separate app into three parts:
    1-ask the user what data they need
    2-request the data from the API
    3-store the data.
"""