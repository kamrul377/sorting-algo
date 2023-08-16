


def bubbleSort(numbers):
    for i in range(0,len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    print(numbers)


numbers = input().split() #input values as string
int_values = [int(num) for num in numbers] #convert integer from string
bubbleSort(int_values) #call the bubbleSort function

