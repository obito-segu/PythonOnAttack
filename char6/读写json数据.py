import json
l = [1,2,'abc',{'name':'Bob','age':13}]
print json.dumps(l,sort_keys=True)
l2 = json.load('[1, 2, "abc", {"age": 13, "name": "Bob"}]')


with open('demo.json','wb') as f:
	json.dump(l2,f)