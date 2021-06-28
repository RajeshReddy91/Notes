"""
which of the following is allowed in python?
1.List inside list
2.Tuple inside list
3.List inside tuple
4.Tuple inside set
5.List as value in Dict
6.Tuple as key in dict
7.Tuple as value in dict
9.Set as value in dict

Note:
    In list and tuple, elements will be inserted based on order and index and PVM won't required any hash.
    Hence elements need not be hashable.
    But in set and dict, elements will be added based on hash. Hence elements should be hashable
    """

supermarket = {
                'store1':{
                            'name':'Kirana stores',
                            'items':[
                                        {'name':'soap', 'quantity':5},
                                        {'name':'brush', 'quantity':15},
                                        {'name':'paste', 'quantity':25}
                                    ]
                         },
                'store2':{
                            'name':'Book Depot',
                            'items':[
                                        {'name':'DS book', 'quantity':15},
                                        {'name':'math book', 'quantity':30},
                                        {'name':'science book', 'quantity':20}
                                    ]
                         }
              }

#print(supermarket)

# to print name of store1
print(supermarket['store1']['name'])
print(supermarket.get('store1').get('name'))

# to print name of all items present in store2
for items in supermarket['store2']['items']:
    print(items['name'])

# how many math books are available
for items in supermarket['store2']['items']:
    if items['name'] == 'math book':
        print('quantity of {} is {}'.format(items['name'],items['quantity']))



