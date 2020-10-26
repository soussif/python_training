#!/usr/bin/env python
"""
Ugly script to iterate through a routing table and print routes.

Lightly modified version of code from Raymond Hettinger's PyCon 2015 talk:

    "Beyond PEP8 -- Best practices for beautiful intelligible code"

This code was originally transliterated from Java into Python. In several
respects it still looks like Java code. In his talk, Hettinger explains how
it can be made much more Pythonic.

Quote from the talk:

> Pythonic means "coding beautifully in harmony with
>   the language to get the maximum benefits from Python".  Learn to recognize
>   non-pythonic APIs and to recognize good code.  Don't get distracted by PEP 8.
>   Focus first on Pythonic versus NonPythonic (P vs NP).  When needed, write
>   an adapter class to convert from the former to the latter.

    * Avoid unnecessary packaging in favor of simpler imports
    * Create custom exceptions
    * Use properties instead of getter methods
    * Create a context manager for recurring set-up and teardown logic
    * Use magic methods:
          __len__ instead of getSize()
          __getitem__ instead of getRouteByIndex()
          make the table iterable
    * Add good __repr__ for better debuggability
'''

"""

from __future__ import print_function

import jnettool.tools.elements
from jnettool.tools import RoutingTable

ne=jnettool.tools.elements.NetworkElement( '171.0.2.45' )
try:
    routing_table=ne.getRoutingTable()  # fetch table

except jnettool.tools.elements.MissingVar:
  # Record table fault
  logging.exception( '''No routing table found''' )
  # Undo partial changes
  ne.cleanup( '''rollback''' )

else:
    num_routes=routing_table.getSize()   # determine table size
    for RToffset in range ( num_routes ):
           route=routing_table.getRouteByIndex( RToffset )
           name=route.getName()       # route name
           ipaddr=route.getIPAddr()          # ip address
           print("%15s -> %s"% (name,ipaddr)) # format nicely
finally:
    ne.cleanup( '''commit''' ) # lockin changes
    ne.disconnect()
