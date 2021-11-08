import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:

        data = {'id': id }
    headers={'content-type':'application/json'}
    json_data = json.dumps(data)

    r = requests.get(url=URL,headers=headers,data=json_data)
   # print('json_data : ',r)
    data = r.json()

    print(data)



#get_data()

def post_data():
    data = {
    
        'name': 'Alok',
        'roll': 'CE-16023',
        'city': 'Tangail'
    }
    headers={'content-type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL,headers=headers,data = json_data)
    data = r.json()
    print(data)
post_data()

def update_data():
    data = {
        'id':5,
        'name': 'Karim',
        'city': 'Rajshahi'
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data = json_data)
    data = r.json()
    print(data)
#update_data()

def delete_data():
    data = {
        'id':3,
    }

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data = json_data)
    data = r.json()
    print(data)
#delete_data()