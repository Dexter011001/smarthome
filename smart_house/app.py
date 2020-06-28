from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
from objects.device import Device,app,db
import uuid 

import os 


@app.route('/devices',methods=['GET'])
def get_all_devices():

    devices = Device.query.all()

    output = []

    for device in devices:
        device_data = {}
        device_data['device_public_id'] = device.device_public_id
        device_data['device_name'] = device.device_name
        device_data['device_state'] = device.device_state
        output.append(device_data)
    
    

    return jsonify({'devices': output})

@app.route('/devices/<device_public_id>', methods=['GET'])
def get_one_user(device_public_id):

    device = Device.query.filter_by(device_public_id=device_public_id).first()

    if not device:
        return jsonify({'message':' No user found'})

    device_data = {}
    device_data['device_public_id'] = device.device_public_id
    device_data['device_name'] = device.device_name
    device_data['device_state'] = device.device_state 

    return jsonify({'Device': device_data})

@app.route('/devices', methods=['POST'])
def add_device():
    data = request.get_json()

    new_device = Device(
        device_name = data['device_name'],
        device_public_id = str(uuid.uuid4()),
        device_state = False
    )

    db.session.add(new_device)
    db.session.commit()

    return jsonify({'message':'New device added!'})

@app.route('/devices/<device_public_id>', methods=['DELETE'])
def delete_device(device_public_id):
    device = Device.query.filter_by(device_public_id=device_public_id).first()

    if not device:
        return jsonify({'message':'No device found'})
    
    db.session.delete(device)
    db.session.commit()

    return jsonify({'message':'device has been deleted'})

@app.route('/devices/<device_public_id>', methods=['PUT'])
def turn_on(device_public_id):
    device = Device.query.filter_by(device_public_id=device_public_id).first()

    if not device:
        return jsonify({'message':'No device found'})
    
    if(device.device_state == True):
        device.device_state = False
        db.session.commit() 
        return jsonify({'message':'Device is off'})
    elif(device.device_state == False):
        device.device_state = True
        db.session.commit() 
        return jsonify({'message':'Device is on'})


@app.route('/devices',methods=['DELETE'])
def delete_all():
    devices = Device.query.all()

    for device in devices:
        db.session.delete(device)
    
    db.session.commit()

    return jsonify({'message':'All devices were deleted'})

if __name__ == '__main__':
    app.run(debug=True)