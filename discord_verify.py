import requests
import os
def verify_user(id):
	url=os.environ['API_URL']
	data={'discord_id':id}
	try:
		res = requests.post(url, json = data)
		if res.json()["result"]=="Id found":
			return True
	except Exception as err:
		print(err)	
	return False	