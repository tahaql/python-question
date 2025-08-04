from collections import Counter


#1
def reverse_string(text):
    return text[::-1]

#2
def most_frequent_number(numbers):
    count = Counter(numbers)
    return count.most_common(1)[0][0]


#3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


#4
def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

#5
def sort_words(sentence):
    words = sentence.split()
    words.sort()
    return ' '.join(words)