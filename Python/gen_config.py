import yaml

yaml_file = open('devices.yml', 'r')

devices = yaml.safe_load(yaml_file)

for item in devices:
    print("Switch", item)
    for interface in devices[item]['interfaces']:
        ip = devices[item]['interfaces'][interface]['ipv4']
        print("interface", interface)
        print("  ip address", ip)
