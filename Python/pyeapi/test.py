import pyeapi
import json


switches = ['leaf1-DC1', 'leaf2-DC1', 'leaf3-DC1', 'leaf4-DC1']

for switch in switches:
    node = pyeapi.connect_to(switch)
    mac_table = node.enable('show mac address-table')
    print("The switch", switch, "knows ", len(mac_table[0]['result']['unicastTable']['tableEntries']), "MAC addresses")
    # for mac in mac_table[0]['result']['unicastTable']['tableEntries']:
    #     print(switch+':', mac['macAddress'])
