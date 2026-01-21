import requests
import json

# Fetch population data from the API and save it to a JSON file
def fetch_data():
    # Define the API endpoint and parameters
    url = "https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/USA_Census_Counties/FeatureServer/0/query"

    params = {
        "where": "1=1",
        "outFields": "STATE_NAME,POPULATION",
        "returnGeometry": "false",
        "f": "json"
    }

    # Make the API request
    response = requests.get(url, params=params)
    data = response.json()


    # Make a dictionary to hold state population data
    state_population = {}

    # for loop through each feature in the response data
    for feature in data['features']:
        state = feature['attributes']['STATE_NAME']
        population = feature['attributes']['POPULATION']

        if population is None:
            continue

        if state not in state_population:
            state_population[state] = 0

        state_population[state] += population

    # for loop to print each state and its population
    for state, population in state_population.items():
        print(f"STATE: {state} | POPULATION: {population}\n")


    # Save the state population data to a JSON file
    with open('state_population.json', 'w') as f:
        json.dump(state_population, f)



    
