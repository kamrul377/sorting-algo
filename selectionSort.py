



def selectionSort(numbers):
    for i in range(0, len(numbers) -1):
        small = i
        for j in range(i+1, len(numbers)):
            if(numbers[j] < numbers[small]):
                small = j
        numbers[i], numbers[small] = numbers[small], numbers[i]
    print(numbers)

numbers = input().split() #input values as string
int_values = [int(num) for num in numbers] #convert integer from string
selectionSort(int_values)

