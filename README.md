# smarthome
Simulator for smarthome. Uses REST api written in flask and mySQL databse

# REST api ussage
GET /devices - Outputs all devices in the house

GET /devices/device_public_id - Outputs one device with the specified device id

POST /devices - Creates a new device 

DELETE /devices/device_public_id - Deletes a device with the specified device id

DELETE /devices - Deletes all devices (FOR DEBUGGING ONLY)

PUT /devices/device_id - Turns on or off a device 

