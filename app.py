import faker

fake = faker.Faker()

names = [fake.name() for _ in range(20)]

print(names)
