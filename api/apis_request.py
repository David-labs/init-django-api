import requests

class RequestHandler:
    BASE_URL = "http://127.0.0.1:8080"
    CREATE_NETWORK_URL = f"{BASE_URL}/network/create"

    @staticmethod
    def functionName(roomNum):
        data = {"id": roomNum}
        
        response = requests.post(RequestHandler.CREATE_NETWORK_URL, json=data)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Request failed with status code {response.status_code}"}

req = RequestHandler()