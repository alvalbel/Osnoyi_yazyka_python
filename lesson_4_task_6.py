# script_one
# from itertools import count
# for i in count(3):
#     print(i)
#     if i == 10:
#         break

# script_two
from itertools import cycle, count
k = 0
for i in cycle('RGY'):
    print(i)
    k += 1
    if k == 10:
        break