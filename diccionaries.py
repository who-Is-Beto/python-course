def run():
  my_diccionary = {
    "name": "Juan",
    "last_name": "Perez",
    "age": 23,
    "city": "Bogota"
  }

  print(my_diccionary["name"])
  print(my_diccionary["last_name"])
  print(my_diccionary["age"])
  print(my_diccionary["city"])

  countries_population = {
    'Argentina': 44_938_712,
    'Brasil': 210_147_125,
    'Colombia': 50_372_424
  }

  for  country in countries_population.keys():
    print('Country:', country)

  for  country in countries_population.values():
    print('Country:', country)

  for  country, population in countries_population.items():
    print(country, 'has:', str(population), 'population')

if __name__ == '__main__':
  run()