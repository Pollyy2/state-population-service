import requests
import json

# The function fetches raw data from the external service, aggregates it by state and stores the result locally as a JSON file
def fetch_data():
    
    url = "https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/USA_Census_Counties/FeatureServer/0/query"

    params = {
        "where": "1=1",
        "outFields": "STATE_NAME,POPULATION",
        "returnGeometry": "false",
        "f": "json"
    }

    # Request data from the ArcGIS REST service
    response = requests.get(url, params=params)
    data = response.json()


    
    state_population = {}

    # Aggregate county population values on state level
    for feature in data['features']:
        state = feature['attributes']['STATE_NAME']
        population = feature['attributes']['POPULATION']

        if population is None:
            continue

        if state not in state_population:
            state_population[state] = 0

        state_population[state] += population

    
    for state, population in state_population.items():
        print(f"STATE: {state} | POPULATION: {population}\n")


    # Save results to a local JSON file
    with open('state_population.json', 'w') as f:
        json.dump(state_population, f)



    
