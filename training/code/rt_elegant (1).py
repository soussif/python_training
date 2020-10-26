"""
Desired code.

From Raymond Hettinger's PyCon 2015 talk: Beyond PEP8
"""

from nettools import NetworkElement

with NetworkElement('171.0.2.45') as ne:
	for route in ne.routing_table:
		print("%15s -> %s" % (route.name, route.ipaddr))
