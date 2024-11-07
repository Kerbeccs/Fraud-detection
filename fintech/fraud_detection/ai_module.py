import requests
import json

API_KEY = 'AIzaSyCxBog3xD111CW86Mqks5T5IuZBx0hvbcQ'  
API_URL = 'https://your-gemini-api-endpoint' 

def predict_fraud(transaction):
   
    payload = {
        'user_id': transaction.user_id,
        'amount': transaction.amount,
        'merchant': transaction.merchant,
        'timestamp': transaction.timestamp.timestamp()  
    }

  
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        prediction = response.json() 
        return prediction  
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None
