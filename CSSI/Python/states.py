states = {
    'CA':'california',
    'AZ':'arizona',
    'AK':'arkansas'
}

for state in states:
    print(' %s is the abbreviation for %s' % (state,states[state]))

store_prices = {
    'cereal': 2.00,
    'stapler': 1.50,
    'fiber-optic': 25.00,
    'lambo':75000

}

store_inventory = {
    'cereal': 750,
    'stapler': 250,
    'fiber-optic':5,
    'lambo':2

}

for price in store_prices:
    store_prices[price]*=1.03


store_inventory['cereal']-=2
store_inventory['lambo']-=1


print(store_prices['cereal']*2 +store_prices['lambo']*2)
print(store_inventory['cereal']-2 + store_inventory['lambo']-2 )
