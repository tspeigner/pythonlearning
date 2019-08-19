import time
import random

num_nums = 100

start_time = time.perf_counter()
numbers = str(random.randint(1,100))
for i in range(num_nums):
    num = random.randint(1,100)
    numbers += ',' + str(num)
end_time = time.perf_counter()
td1 = end_time - start_time

start_time = time.perf_counter()
numbers=[]
for i in range(num_nums):
    num = random.randint(1,100)
    numbers.append(str(num))
numbers = ', '.join(numbers)
end_time = time.perf_counter()
td2 = end_time - start_time

start_time = time.perf_counter()
numbers = [str(random.randint(1,100)) for i in range(1,num_nums)]
numbers = ', '.join(numbers)
end_time = time.perf_counter()
td3 = end_time - start_time

print('''Number of numbers: {:,}
Time Delta 1: {}
Time Delta 2: {}
Time Delta 3: {}'''.format(num_nums, td1, td2, td3))