import requests

out_data = {"name": "Jiby Krishna",
            "net_id": "jk562",
            "e-mail": "jiby.kg@duke.edu" }

r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json = out_data)
print(r.status_code)
print(r.text)

r = requests.post("http://vcm-21170.vm.duke.edu:5000/list", json = out_data)
print(r.status_code)
print(r.text)