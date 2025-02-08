
def fibonnaci_recursion(n):
        if (n < 0):
            #Input validation
            print("Invalid Input")
        #Base Case 1
        elif(n == 0):
            result = 0
            return result
        #Base Case 2
        elif (n == 1 or n == 2):
            result = 1
            return result
        else:
            #Calling the recursive function
            result = fibonnaci_recursion(n - 1) + fibonnaci_recursion(n-2)
            return result
        
# Getting the input value from user
n = input("Enter the number of terms for the Fibonacci Sequenece: ")

#Converting the input to an integer
n = int(n)

#Displaying the results
print("The Sum of the Fibonnacci Sequence: " + str(fibonnaci_recursion(n)))