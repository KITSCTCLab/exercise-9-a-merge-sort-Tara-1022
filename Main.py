from typing import List

def merge(l1: [int], l2: [int]) -> [int]:
  new = [0] * (len(l1) + len(l2))
  i, j = 0, 0
  k =  0
  while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
      new[k] = l1[i]
      i += 1
    else:
      new[k] = l2[j]
      j += 1
    k += 1
  while i < len(l1):
    new[k] = l1[i]
    i += 1
  while j < len(l2):
    new[k] = l2[j]
    j += 1
  return new

def merge_sort(data) -> None:
  if len(data) <= 1:
    return
  mid = len(data)//2
  data = merge(merge_sort(data[:mid]), merge_sort(data[mid:]))
  return data


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
