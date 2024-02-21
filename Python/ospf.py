import yaml

raw_yaml = open('ospf.yml', 'r')

ospf_config = yaml.safe_load(raw_yaml)

# Set some global variables from YAML

mtu = ospf_config['global_settings']['mtu']

config_directory = "configs"


for device in ospf_config['devices']:
    # Open file to write
    file = 'configs/'+ device + '.txt'
    f = open(file, )
    print("This config is for", device)
    lo0 = ospf_config['devices'][device]['loopbacks']['loopback0']
    # p2p Interfaces
    for p2p in ospf_config['devices'][device]['p2p']:
        print("interface", p2p)
        print("  no switchport")
        print("  ip address unnumbered loopback0")
        print("  mtu", mtu)
        print("  ip ospf area 0")
        print("  ip ospf network point-to-point")
    # OSPF Router
    print("ip routing")
    print("router ospf 10")
    print("  router-id", lo0)
    # Configure loopback
    for loopback in ospf_config['devices'][device]['loopbacks']:
        loopback_ip = ospf_config['devices'][device]['loopbacks'][loopback]
        print("interface", loopback)
        print("  ip address", loopback_ip+'/32')
        print("  ip ospf area 0")