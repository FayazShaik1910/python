#Reverse a given string without using built-in reverse functions
def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

print(reverse_string(input(" enter name: ")))


# Check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False

#Count the number of vowels and consonants in a string
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count, c_count = 0, 0
    
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

print(count_vowels_consonants("Hello World"))
#Remove all spaces from a given string
def remove_spaces(s):
    result = ""
    for ch in s:
        if ch != " ":
            result += ch
    return result

print(remove_spaces("Hello World Python"))
#Count the frequency of each character in a string
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_frequency("banana"))



