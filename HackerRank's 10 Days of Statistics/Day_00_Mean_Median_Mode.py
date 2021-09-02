# I avoided using library despite their ability to save my time.
# To be honest, these are my first Python code in a while
# I haven't used Python for about 2-3 months, so maybe my code style is not clean enough. Pardon me if there are any issues.

# Get the input parameters
N = int(input())
X = input()
numbers = [int(x) for x in X.split()]

# Mean
tong = 0.0
for num in numbers:
    # I'm afraid of big numbers, so I divide each number for N before calculating.
    tong += num/N
print(round(tong, 1))
 
numbers.sort()
# Median
if N % 2 == 0:
    median1 = numbers[N//2]
    median2 = numbers[N//2 - 1]
    median = median1/2 + median2/2
else:
    median = numbers[N//2]
print(median)

# Mode
mode = -1
maxCount = 0
for i in range(len(numbers)):
    currentNum = numbers[i]
    count = 1
    for j in range(i, len(numbers)):
        if numbers[j] == currentNum:
            count += 1
            if count > maxCount:
                maxCount = count
                if maxCount == 1:
                    mode = numbers[0]
                else:
                    mode = currentNum
print(mode)
