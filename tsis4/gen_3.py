n = int(input("Enter a number: "))
divisible_nums = [num for num in range(n+1) if num % 3 == 0 and num % 4 == 0]
print(divisible_nums)
