import json
from napalm import get_network_driver

# ios_driver = get_network_driver('ios')
# iosvl2 = ios_driver('192.168.108.126', 'faek', 'faek')
# iosvl2.open()
# ios_output = iosvl2.get_facts()
# print(json.dumps(ios_output, indent=5))
# iosvl2.close()


# driver = get_network_driver('eos')
# eosl2 = driver('192.168.108.128', 'faek', 'faek')
# eosl2.open()
# eos_output = eosl2.get_facts()
# print(json.dumps(eos_output, indent=4))
# eosl2.close()

ios_driver = get_network_driver('ios')
iosvl2 = ios_driver('192.168.108.126', 'faek', 'faek')
iosvl2.open()
ios_output = iosvl2.get_interfaces()
print(json.dumps(ios_output, indent=5))
iosvl2.close()


driver = get_network_driver('eos')
eosl2 = driver('192.168.108.128', 'faek', 'faek')
eosl2.open()
eos_output = eosl2.get_interfaces()
print(json.dumps(eos_output, indent=4))
eosl2.close()