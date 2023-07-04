from fastapi import FastAPI
import requests


app = FastAPI()

@app.get("/")
def api_request():
    """API call on catfact.ninja
    
    When directly calling it on postman the response is return after 250ms
    but when I used this code it returns after 800ms
    """
    url = "https://catfact.ninja/breeds?limit=10"
    response = requests.get(url)
    return response.json()
