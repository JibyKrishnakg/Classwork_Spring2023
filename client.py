import requests

server = "http://127.0.0.1.5000"

r = requests.get(server + "/info")
print(r.status_code)
print(r.text)

out_data = {"name": "Jiby", "HDL_value": 60}
r = requests.get(server + "/HDL_analysis", json=out_data)
print(r.status_code)
print(r.text)

r = requests.get(server + "/add_two/five/26")


out_data = {"a": 2, "b": -3}
r = requests.get(server + "/add", json=out_data)
print(r.status_code)
print(r.text)
if r.status_code == 200:
    x = r.json()
    print(x + 2)