# coding: utf-8
# Based on example from http://ozgur.github.io/python-firebase/
from firebase import firebase

# firebase = firebase.FirebaseApplication('https://boiling-fire-1432.firebaseio.com/', None)
# data = {'name': 'Actuarial services', 'location' : 'Paris', 'created at': 2016} 
# firebase.post('/locationData', data)
# result = firebase.get('/X', None)
# print(result)

def pushFireBase(data, url, dataName):
	# Erases previous data version and pushes new one
	try:
		firebase = firebase.FirebaseApplication(url, None)
		firebase.delete(dataName)
		firebase.post(dataName, data)
		return True
	except:
		return False