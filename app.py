# example from http://ozgur.github.io/python-firebase/
from firebase import firebase
firebase = firebase.FirebaseApplication('https://boiling-fire-1432.firebaseio.com/', None)
result = firebase.get('/users', None)
print(result)