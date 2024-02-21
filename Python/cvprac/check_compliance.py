from cvprac.cvp_client import CvpClient
import requests

# This removes the validation warnings for Self Signed Certificates
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = "192.168.0.5"
cvp_user = "arista"
cvp_pw = "aristaxp3t"

client = CvpClient()

client.connect([cvp1], cvp_user, cvp_pw)

inventory = client.api.get_inventory()


for item in (inventory):
    if item['complianceCode'] == "0001":
        print(item['hostname'], "is out of configuration compliance")
