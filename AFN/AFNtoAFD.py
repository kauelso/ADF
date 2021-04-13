import json

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

with open('AFN/AFNjson.json','r') as json_file:
    AFNjson = json.load(json_file)

E = AFNjson['E']
Q = AFNjson['Q']
Q0 = AFNjson['Q0']

print(list(powerset([1,2,3])))
