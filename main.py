import requests, json
params = {
    "key" : "e16921e57e084bc7873184420251512",
    "q" : "Paris"
}
response = requests.get("http://api.weatherapi.com/v1/current.json", params=params)
print(response.status_code)

def get_data():
    weather_data = response.json()
    print(f"temperatura: {weather_data["current"]["temp_c"]} grados")

if response.status_code == 200:
    get_data()    
    
    
    """separate app into three parts:
    1-ask the user what data they need
    2-request the data from the API
    3-print the requested data
    """