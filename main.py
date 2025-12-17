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
                API_request = "current.json"
            elif request_type == "2":
                API_request = "forecast.json"
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
    return city, API_request

       
def get_weather(city, API_request):
    params = {
        "key" : "e16921e57e084bc7873184420251512",
        "q" : city
    }
    response = requests.get(f"http://api.weatherapi.com/v1/{API_request}", params=params)
    print(response.status_code)


    weather_data = response.json()
    try:
        print(f"temperatura: {weather_data['current']['temp_c']} grados")
    except KeyError:
        print("something went wrong. perhaps you asked for an invalid city?")
    if response.status_code == 200:
        #get_data()
        pass
    

if __name__ == '__main__':
    city, API_request = main()
    get_weather(city, API_request)


    
    
    """separate app into three parts:
    1-ask the user what data they need
    2-request the data from the API
    3-print the requested data
"""