#! /usr/bin/env python3

from senzing import G2Engine, G2Exception

# REPLACE /home/user/tryme with the path to your Senzing project created in the quickstart
config = '{"PIPELINE" : {"CONFIGPATH" : "/etc/opt/senzing","RESOURCEPATH" : "/opt/senzing/g2/resources","SUPPORTPATH" : "/opt/senzing/data"},"SQL" : { "CONNECTION" : "postgresql://max:mugrumph1@172.17.0.1:5432:testdb" }}'


record = '{ "NAME_FULL": "JOHN SMITH", "ADDR_FULL": "123 Main St, Las Vegas NV" }'

try:

  # Initialize the G2Engine
  g2 = G2Engine()
  g2.init("DoIT",config,False)

  # Entity resolve a record
  g2.addRecord("TEST","1",record)

  # Get the entity it resolved to
  response = bytearray()
  g2.getEntityByRecordID("TEST","1",response)

  # Display entity JSON
  print(response.decode())

  # Search for entities
  g2.searchByAttributes('{ "NAME_FIRST": "JANE", "NAME_LAST": "SMITH", "ADDR_FULL": "123 Main St, Las Vegas NV" }', response)

  # Display result JSON
  print(response.decode())

except Exception as err:
  print(err)
