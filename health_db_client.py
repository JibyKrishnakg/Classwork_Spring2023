import requests
server = "https://127.0.0.1.5000"
patient = {"id": 1, "name": "Jiby","blood_type": "O+"}
r = requests.post(server + "/new_patient", json=patient)
print(r.status_code)
print(r.text)

