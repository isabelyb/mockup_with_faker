from faker import Faker
from faker.providers import internet # Faker IPs


fake = Faker()

fake.name()
fake.address()
fake.text()

def names():
    names = []
    for _ in range(10):
        name = fake.name()
        names.append(name)
    return names


# To print 10 faker names
for _ in range(10):
  print(fake.name())

# To get IP
fake.add_provider(internet)
print(fake.ipv4_private())

#Localization
fake = Faker('it_IT')
for _ in range(10):
    print(fake.name())



f = open("demofile2.sql", "a")
f.write(f'{names()}')
f.close()