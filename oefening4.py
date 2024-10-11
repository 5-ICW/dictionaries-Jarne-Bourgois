


fruit = {
    "appel":5.00,
    "banaan":4.00,
    "peer":6.00,
    "druif":1.00,
    "citroen":2.00,

}

def prijzen(prijs_fruit):
    
    return sum(prijs_fruit.values())



print(prijzen(fruit))