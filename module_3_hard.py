def calculate(item):
    global add
    if isinstance(item, int):
      add += item
    elif isinstance(item, str):
      add += len(item)
    elif isinstance(item, (list, tuple, set)):  #[1, (2, 2, 3), 3]
      for i in item:
          calculate(i)
    elif isinstance(item, dict):
      for key, value in item.items():
        calculate(key)
        calculate(value)


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
add = 0
calculate(data_structure)
print(add)