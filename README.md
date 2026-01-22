# USA States Population API

A simple FastAPI backend that provides US state population data.

- Fetches population data from a REST service for all US counties.
- Aggregates population per state and saves it in `state_population.json`.
- REST API endpoints:
  - `GET /states` → all states
  - `GET /states/{state_name}` → specific state
- Handles missing file and unknown state errors.

## Run

```bash
pip install fastapi uvicorn requests
uvicorn main:app --reload
