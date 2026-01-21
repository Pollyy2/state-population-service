from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# Endpoint to get population data for all states
@app.get("/states")
def get_states():
    try:
        # Load the state population data from the JSON file
        with open('state_population.json', 'r') as f:
            state_population = json.load(f)  

        # return the data as a dictionary
        return state_population
    # if the file does not exist, raise a 404 error
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found.")
    
# Endpoint to get population data for a specific state
@app.get("/states/{state_name}")
def get_state_population(state_name: str):
    try:
        with open('state_population.json', 'r') as f:
            state_population = json.load(f)

        population = state_population.get(state_name)
        # if the state is not found, raise a 404 error
        if population is None:
            raise HTTPException(status_code=404, detail="State not found")

        
        return {"state": state_name, "population": population}  
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found.")