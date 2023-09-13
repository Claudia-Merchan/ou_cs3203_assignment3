def sumList(givenList):
    Sum = sum(givenList)
    return Sum

def multiplyList(givenList):
    product = 1
    for n in givenList:
        product = product * n
    return product

def main():
    userInput = input("Input a list of numbers separated by spaces: ")
    userList = [int(x) for x in userInput.split()]
    userSum = sumList(userList)
    userProduct = multiplyList(userList)

    print("Sum: ", userSum, '\n')
    print("Product: ", userProduct)
    #comment for part 10 of assigmnet three so that there is a change in the code

if __name__ == "__main__":
    main()

def reverse(givenList):
    revList = givenList.reverse()
    return revList