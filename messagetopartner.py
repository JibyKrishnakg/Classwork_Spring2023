import requests

outdata = {"user": "Jiby", "message": "Hello, this is Jiby"}

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=outdata)
print(r.text)

r_get = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Shanshan")
print(r_get.text)