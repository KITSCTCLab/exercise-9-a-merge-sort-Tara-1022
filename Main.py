from typing import List

def merge(arr: [int], l: int, mid: int, r: int) -> [int]:
  l1 = arr[l:mid]
  l2 = arr[mid:r]
  i, j = 0, 0
  k =  l
  while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
      arr[k] = l1[i]
      i += 1
    else:
      arr[k] = l2[j]
      j += 1
    k += 1
  while i < len(l1):
    arr[k] = l1[i]
    i += 1
    k += 1
  while j < len(l2):
    arr[k] - l2[j]
    j += 1
    k += 1

def merge_sort_ftn(arr, l, r) -> None:
  if r - l >= 2:
    mid = l + (r - l) // 2
    merge_sort_ftn(arr, l, mid)
    merge_sort_ftn(arr, mid, r)
    merge(arr, l, mid, r)
  
def merge_sort(data) -> None:
  merge_sort_ftn(data, 0, len(data))


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
