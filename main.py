def word_count(words):
    word = words.split()
    return len(word)

def longest_word(words):
    word = words.split()
    longest = max(word, key=len)
    return longest

def reverse_sentence(words):
    return words[::-1]

def prime_number(num):
    if num > 1:
        count = 0
        for i in range(2,num):
            if (num % i) == 0:
                count = count + 1
            else:
                continue
        if count ==0:
            return f"{num} is a prime number"
        else:
            return f"{num} is not a prime number"
    elif num ==1:
        return "1 is not a prime number"
    else:
        return "Enter a number bigger than 1"

#getting input from user    
word = input("Enter a sentence: ")    
num = int(input("Enter a number: "))

#displaying results
print("\n------Sentence Analysis------")
print(f"Word count: {word_count(word)}")
print(f"Longest word: {longest_word(word)}")
print(f"Reversed sentence: {reverse_sentence(word)}")

print("\n------Prime Number Check------")
print(prime_number(num))
