import requests

r_get = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/jk562")
print(r_get.text)


r_get1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M6")
print(r_get1.text)

r_get2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F6")
print(r_get2.text)

outdata1 = {"Name": "jk562", "Match":  "Yes"}
           
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=outdata1)
print(r.text)
