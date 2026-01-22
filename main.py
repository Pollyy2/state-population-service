from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# Returns population data for all states
@app.get("/states")
def get_states():
    try:
        # Data is read from a pre-generated JSON file
        with open('state_population.json', 'r') as f:
            state_population = json.load(f)  

        
        return state_population
    # File is missing if background processing hasn't been run yet
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found.")
    
# Returns population data for a single state based on its name
@app.get("/states/{state_name}")
def get_state_population(state_name: str):
    try:
        with open('state_population.json', 'r') as f:
            state_population = json.load(f)

        population = state_population.get(state_name)
        
        if population is None:
            raise HTTPException(status_code=404, detail="State not found")

        
        return {"state": state_name, "population": population}  
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found.")