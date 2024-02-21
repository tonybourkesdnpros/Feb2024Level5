from cvprac.cvp_client import CvpClient
import requests
import os
import time 

# This removes the validation warnings for Self Signed Certificates
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


cvp1 = "192.168.0.5"
cvp_user = "arista"
cvp_pw = "aristaxp3t"

client = CvpClient()

client.connect([cvp1], cvp_user, cvp_pw)

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

configlets = client.api.get_configlets(start=0, end=0)



current_datetime = time.strftime("%Y%m%d-%H%M%S")
current_directory = directory+"/"+current_datetime

os.makedirs(current_directory)
for item in (configlets['data']):
    print("Writing the configlet", item['name'], "to file")
    file_name = item['name'] + ".txt"
    file = open(current_directory+"/"+file_name, 'w')
    file.write(item['config'])
    file.close()


2024_02_21_14_43_00