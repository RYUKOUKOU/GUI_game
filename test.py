import random

# 生成10个不重复的随机数，范围在1到1078之间
random_numbers = random.sample(range(1, 1079), 10)

print("生成的随机数:", random_numbers)
