# Coding Challenge 2

For this coding challenge, for each item below produce a Python file that addresses each task (total of 5 files in your repo):

### 1. List values

Using this list:

```python
[1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
```
You need to do two separate things here and report both in your Python file. You should have two solutions in this file, one for item 1 and one for item 2. Item 2 is tricky so if you get stuck try your best (no penalty), for a hint check out the solution by desiato [here](https://stackoverflow.com/questions/32580489/python-for-and-if-on-one-line).

1. Make a new list that has all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python (you do not need to append to a list just print the output).



### 2. List overlap

Using these lists:

```python
list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
```

1. Determine which items are present in both lists.
2. Determine which items do not overlap in the lists.

### 3. Given a singe phrase, count the occurrence of each word

Using this string:

```Python
string = 'hi dee hi how are you mr dee'
```
1. Count the occurrence of each word, and print the word plus the count (hint, you might want to "split" this into a list by a white space: " ").

### 4. User input

Ask the user for an input of their current age, and tell them how many years until they reach retirement (65 years old).

Hint:

```Python
age = input("What is your age? ")
print "Your age is " + str(age)
```

### 5. User input 2

Using the following dictionary (or a similar one you found on the internet), ask the user for a word, and compute the *Scrabble* word score for that word (Scrabble is a word game, where players make words from letters, each letter is worth a point value), steal this code from the internet, format it and make it work:

```python
letter_scores = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}
```
