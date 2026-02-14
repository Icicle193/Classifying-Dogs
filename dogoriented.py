class dog:

    def __init__(self, breed, name, color):
        self.breed = breed
        self.name = name
        self.color = color

poodle = dog('Poodle', 'dog', 'goldish')
dalmation = dog('Dalmation', 'dog', 'white with black spots')

print(poodle.breed, ",", poodle.name, ",", poodle.color)
print(dalmation.breed, ',', dalmation.name, ',', dalmation.color)