#!/usr/bin/python
import sys
import os
import xml.etree.ElementTree
import urllib.request,urllib.parse
import json
import socket
import time
import random
import string


baseUrl = 'http://localhost:8082'
user = { 'email' : 'admin', 'password' : 'admin' }
debug = '-v' in sys.argvvehicle 1 	online 	13322 	3
def login():
    request = urllib.request.Request(baseUrl + '/api/session')
    response = urllib.request.urlopen(request, urllib.parse.urlencode(user).encode("utf-8"))
    if debug:
        print ('\nlogin: %s\n' % repr(json.load(response)))
    return response.headers.get('Set-Cookie')

def id_generator(x):
    size=5
    chars=chars=string.ascii_uppercase + string.digits
    return 'vehicle'.join(x)

def add_device(cookie, unique_id):
    request = urllib.request.Request(baseUrl + '/api/devices')
    request.add_header('Cookie', cookie)
    request.add_header('Content-Type', 'application/json')
    device = { 'name' : 'vehicle'+''+str(unique_id)+'', 'uniqueId' : unique_id }
    print(request)
    response = urllib.request.urlopen(request, json.dumps(device).encode("utf-8"))
    data = json.load(response)
    return data['id']

def add_drivers(cookie, unique_id):
    request = urllib.request.Request(baseUrl + '/api/drivers')
    request.add_header('Cookie', cookie)
    request.add_header('Content-Type', 'application/json')
    device = { 'name' : 'driver'+''+str(unique_id)+'', 'uniqueId' : unique_id }
    print(request)
    response = urllib.request.urlopen(request, json.dumps(device).encode("utf-8"))
    data = json.load(response)
    return data['id']

cookie = login()

for x in range(10):
    x : add_device(cookie, x)
    x : add_drivers(cookie, x+100)
    
