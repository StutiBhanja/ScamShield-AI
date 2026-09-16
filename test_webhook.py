import requests

url = "https://stutibhanja28.app.n8n.cloud/webhook-test/8a6465c3-634d-4e26-ab94-0f793649cf5d"

data = {
    "message": "Congratulations! You have won ₹50,000. Pay ₹499 processing fee immediately to claim your prize."
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.text)