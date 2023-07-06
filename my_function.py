# Create a Python file called my_function.py 

# created a def function that returns the days of the week  
def days_of_the_week():
    print("Monady")
    print("Tuesday")
    print("Wednesday")
    print("Thursday")
    print("friday")
    print("saturday")
    print("sunday")

days_of_the_week()

# def function takes in user_input as a parameter
def making_a_sen (sentence):
    sentence = input("create a sentance:" )
    
# declared an empty string     
    new_string = ""

    index = 0

# Iterates through all words of the sentence using a for_loop and splits it 
# If i % 2 is equal to 1 it adds hello to the string sentence 
# returns an updated sentence with every second word with hello    
    for i in sentence.split():

        if index % 2 == 1:
            new_string += "hello "
        else:
            new_string+= i + " "

        index += 1

# removes the last space at the end
    sentence = sentence[:-1]

    print(new_string)

making_a_sen(input)


    
    






