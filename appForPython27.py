from firebase import firebase
import pdb

fb = firebase.FirebaseApplication('https://boiling-fire-1432.firebaseio.com/', None)
new_user = 'Sammy Khalife'
result = fb.post('/users', new_user, {'print' : 'pretty'})
pdb.set_trace()
