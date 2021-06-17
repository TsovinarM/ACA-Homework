num_0 = int(input())
num_1 = num_0 % 10
num_2 = (num_0 % 100) // 10
num_3 = (num_0 % 1000) // 100
num_4 = (num_0 // 1000)
sum = num_1 + num_2 + num_3 + num_4
print (sum)