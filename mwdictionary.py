# Theo Xiong 2021/3/10
# Wrapper for the Merriam-Webster dictionary API

import requests
import json

class MWDictionary():

	KEY = ""

	def __init__(self, key):
		self.KEY = key

	def define(self, word):
		if not word or word.isspace():
			res = {
			'word': 'null',
			'definition': 'null',
			'type': 'null',
			'offensive': 'null'
			}
			return res
		url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'
		geturl = url + word + '?key=' + self.KEY
		req = requests.get(geturl)
		req_text = json.loads(req.text)
		try:
			res = {
			'word': word,
			'definition': req_text[0]['shortdef'][0],
			'type': req_text[0]['fl'],
			'offensive': str(req_text[0]['meta']['offensive'])
			}
		except:
			res = {
			'word': word,
			'definition': 'null',
			'type': 'null',
			'offensive': 'null'
			}
		return res

