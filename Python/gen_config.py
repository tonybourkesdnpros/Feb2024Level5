import yaml

mtu = 9214
yaml_file = open('devices.yml', 'r')

devices = yaml.safe_load(yaml_file)

for item in devices:
    print("Switch", item)
    for item2 in devices[item]['interfaces']:
        ip = devices[item]['interfaces'][item2]['ipv4']
        print("interface", item2)
        if "thernet" in item2:
            print("  no switchport")
            print("  mtu", mtu)
        print("  ip address", ip)