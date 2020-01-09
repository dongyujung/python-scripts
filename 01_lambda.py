# Lambda function
double = lambda x: x * 2
print(double(3))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# Filter
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
# Map
mapped_list = list(map(lambda x: x ** 2, my_list))
print(filtered_list)
print(mapped_list)