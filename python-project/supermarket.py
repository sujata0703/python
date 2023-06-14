l1=[
    { 'name':'soap', 'qty':20},
    {'name':'brush','qty':10},
    { 'name':'pen', 'qty':30},
]
l2=[
    { 'name':'Django', 'qty':50},
    {'name':'python','qty':60},
    { 'name':'java', 'qty':70},
]


supermarket={
            'store1':{'name':'durgageneralstore','items' :l1},
             'store2':{'name':'durgabookstore','items' :l2}

             }

print(supermarket)
print('supermarketstore1name',supermarket.get('store1').get('name'))
print(supermarket['store1']['items'])
print(supermarket['store2']['items'])
print('no of python books available')
for d in supermarket['store2']['items']:
    if d['name'] == 'python':
        print(d['qty'])













