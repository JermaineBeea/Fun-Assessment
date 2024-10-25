def dog_years(age_in_human_years):
    
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """
    threshold = 20
    if age_in_human_years <= 20:
        is_over_2 = age_in_human_years > 2
        return age_in_human_years * 10.5 if is_over_2  else  2 * 10.5 + (age_in_human_years - 2)*4
    else:
        raise ValueError (f'Dog age in human years cannot be greater than {threshold} ')

 
def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """

    if not isinstance(num, (float, int)):
        raise TypeError(f'Invalid type [{type(num)}] num must be of type int or float')
    
    list_return = []

    for number in range(1, num + 1):
        case_1 = number % 3 == 0 and number > 1
        case_2 = number % 5 == 0 and number > 1
        case_3 = case_1 and case_2

        if case_3:
            list_return.append('FizzBuzz')
        
        elif case_2: 
            list_return.append('Buzz')
        
        elif case_1: 
            list_return.append('Fizz')
        
        else: 
            list_return.append(str(number))
    
    return ' '.join(list_return)
        

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    #enter your code here    
    split_sent = sentence.split()
    dictionary = {word: len(word) for word in split_sent}

    return dictionary
    

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
    sum = 0
    str_number = list(str(number))

    for num in str_number:
        num = int(num)
        sum += num ** 3
    
    return sum


Test_func = dog_years
input =  10

print(Test_func(input))