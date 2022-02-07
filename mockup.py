from faker import Faker

fake = Faker()

for _ in range(1000):
  print(fake.name())



