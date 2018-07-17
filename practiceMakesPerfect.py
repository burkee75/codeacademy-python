# Factorial

# All right! Now we're cooking. Let's try a factorial problem.
# To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example:

# factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
# factorial(1) would equal 1.
# factorial(3) would equal 3 * 2 * 1, which is 6.


def factorial(x):
  print('x is ', x)
  answer = 1
  while x > 0:
        answer = answer * x
        print("answer is ", answer)
        x -= 1
        print('now x is ', x)
  return answer

factorial(2)



# is_prime
# A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. (That's a mouthful!)
# In other words, if you want to test if a number in a variable x is prime, then no other number should go into x evenly besides 1 and x. So 2 and 5 and 11 are all prime, but 4 and 18 and 21 are not.
# If there is a number between 1 and x that goes in evenly, then x is not prime.

# Define a function called is_prime that takes a number x as input.
#F or each number n from 2 to x - 1, test if x is evenly divisible by n.
# If it is, return False.
#I f none of them are, then return True.

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True


# Reverse
# Define a function called reverse that takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".
# You may not use reversed or [::-1] to help you with this.
# You may get a string containing special characters (for example, !, @, or #).

def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

