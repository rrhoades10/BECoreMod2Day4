import re
'''
1. **Dot (.)**
    - The wildcard: Matches any single character except newline (`\n`).
    - Imagine it as a shape-shifter, able to become any character you need, just for a moment.
2. **Caret (^)**
    - The anchor for the start of a string.
    - Like a sentinel, standing guard at the beginning of your text.
3. **Dollar ($)**
    - The anchor for the end of a string.
    - The sentinel at the gates, ensuring nothing goes beyond the end of your text.
4. **Asterisk (*)**
    - Matches zero or more occurrences of the pattern left to it.
    - Think of it as a multiplier, creating copies of the character before it.
5. **Plus (+)**
    - Matches one or more occurrences of the pattern left to it.
    - Similar to the asterisk, but insists on at least one occurrence.
6. **Question Mark (?)**
    - It makes the preceding character optional.
    - It's the symbol of uncertainty, allowing flexibility in your patterns.
7. **Backslash (\)**
    - Escapes special characters or signals a special sequence.
    - The key to differentiating between a literal character and a magical symbol.
8. **Square Brackets ([])**
    - A set of characters. Matches any one character in the brackets.
    - Like choosing one tool from a toolbox, it selects one character from a set.
9. **Pipe (|)**
    - The OR operator. It matches either the pattern before or after it.
    - A fork in the road, giving you a choice between paths.
10. **Parentheses (())**
    - Groups patterns together and captures them.
    - Think of them as binding a spell, containing its power within.
11. **Curly Braces ({})**
    - Curly braces are used to define the exact number of times a character or a pattern must occur for a match to be found.
    - It's like telling your magic spell exactly how much power to use.
'''
### **Simple Exercises for Understanding**


'''
1.  **Dot (.) - The Wildcard Character**
    - **Task**: Find any three-character sequence in a text, where the middle character can be anything, the first has to be ‘c’ and the last has to be ‘t’.
    - **Regex Pattern**: `c.t`
    - **Test Sentence**: "I found a cat, a cot, and a cut in the room and the cat was cute, ctt cct coot colt"
    - **Expected Matches**: `['cat', 'cot', 'cut', cat, cut]`
    - **Explanation**: The dot `.` matches any single character (except newline), so it finds sequences where 'c' and 't' are separated by any character.
2. **Caret (^) - The Beginning Anchor**
    - **Task**: Find strings that start with 'Py'.
    - **Regex Pattern**: `^Py`
    - **Test Sentence**: "Python is fun"
    - **Expected Matches**: `[’Py’]` from 'Python' at the beginning of the sentence.
    - **Explanation**: The caret `^` ensures that the match must occur at the start of the string or line.
3. **Dollar ($) - The End Anchor**
    - **Task**: Identify strings that end with 'fun'.
    - **Regex Pattern**: `fun$`
    - **Test Sentence**: "Learning regex is fun"
    - **Expected Matches**: `['fun']` from 'Learning regex is fun.'
    - **Explanation**: The dollar `$` ensures that 'fun' is matched only if it's at the end of the string or line.
4. **Asterisk (*) - Zero or More Occurrences**
    - **Task**: Match a character followed by zero or more 'a's.
    - **Regex Pattern**: `ba*`
    - **Test Sentence**: "I saw a bat, and a ball in my bed, baaah!"
    - **Expected Matches**: `['ba', 'ba', 'b', 'baaa']` from ‘bat’, ‘ball’, ‘bed’, and ‘baaah!’.
    - **Explanation**: The pattern starts with the literal character 'b'. This means it will first look for occurrences of 'b' in the text. Following the 'b', we have 'a*'. Then, the asterisk  `*` which matches zero or more occurrences of the preceding character ('a' in this case).
5. **Plus (+) - One or More Occurrences**
    - **Task**: Find a character followed by one or more 'a's.
    - **Regex Pattern**: `ba+`
    - **Test Sentence**: "The battle of ba and baat."
    - **Expected Matches**: `['ba', 'ba', 'baa']` from ‘battle’, ‘ba’, and ‘baat’.
    - **Explanation**: The plus `+` matches one or more occurrences of the preceding character ('a' in this case).
6. **Question Mark (?) - Zero or One Occurrence**
    - **Task**: Match 'colour' or 'color'.
    - **Regex Pattern**: `colou?r`
    - **Test Sentence**: "The color is nice. I like this colour."
    - **Expected Matches**: `['color', 'colour']`
    - **Explanation**: The question mark `?` makes the preceding character ('u' in this case) optional.
7. **Backslash (\) - Escaping Special Characters**
    - **Task**: Match a period character in a sentence.
    - **Regex Pattern**: **`\.`**
    - **Test Sentence**: "End of sentence. Start of a new one."
    - **Expected Matches**: The periods `[.]` at the end of 'sentence.' and before 'Start'.
    - **Explanation**: In regex, the period (.) is a special character used as a wildcard. To match an actual period, the backslash **`\`** is used to escape the special meaning of the period, treating it as a literal character. The pattern **`\.`** specifically looks for the period character in the text.
8. **Square Brackets ([]) - Character Sets**
    - **Task**: Find all vowels in a word.
    - **Regex Pattern**: `[aeiou]`
    - **Another Pattern**: `[A-Za-z+]` - 
    - **Test Word**: "Regular"
    - **Expected Matches**: `['e', 'u', 'a']`
    - **Explanation**: The square brackets `[]` define a set of characters, any of which can be matched.
9. **Pipe (|) - The OR Operator**
    - **Task**: Match 'cat' or 'dog'.
    - **Regex Pattern**: `cat|dog`
    - **Test Sentence**: "I have a cat and a dog."
    - **Expected Matches**: `['cat', 'dog']`
    - **Explanation**: The pipe `|` acts as an OR operator, matching either the pattern before or after it.
10. **Parentheses (()) - Grouping**
    - **Task**: Find repetitions of 'woof' or 'meow'.
    - **Regex Pattern**: `(woof|meow)+`
    - **Test Sentence**: "The pets say woof woof and meow."
    - **Expected Matches**: `['woof’,  'woof', 'meow']`
    - **Explanation**: Parentheses `()` group patterns, allowing the plus `+` to apply to the entire group.
11. **Curly Braces ({}) - Specifying Exact Occurrences**
    - **Task**: Match a word where 'l' is followed by exactly two 'o's.
    - **Regex Pattern**: **`lo{2}`**
    - **Regex Pattern**: **`[L|lo{2}]`**
    - **Regex Pattern**: **`[A-Z|a-zo{2}]`**
    - **Test Sentence**: "Look at the loom and the balloon in the room, loser."
    - **Expected Matches**: ['loo', 'loo']
    - **Explanation**: The pattern **`lo{2}`** searches for an 'l' followed by exactly two 'o's. In our test sentence, it successfully identifies 'loo' within the words 'loom' and 'balloon', demonstrating the ability of curly braces **`{}`** to specify an exact number of occurrences.

'''

## Deciphering the Code of Special Sequences in Regular Expressions

### **Special Sequences and Their Magical Powers**
'''
Special sequences in regex are like shortcuts or spells. Each one has a specific purpose and helps us find exactly what we’re looking for with minimal fuss. Here are some of the most commonly used sequences:

1. **\d - The Digit Hunter**
    - Hunts down digits (0-9) in your text.
    - It's like a metal detector that beeps only when it finds numbers.
2. **\w - The Word Wizard**
    - Finds word characters (letters, digits, and underscores).
    - Imagine it as a magnet that attracts only words and numbers, leaving everything else behind.
3. **\s - The Space Scout**
    - Seeks out whitespace (spaces, tabs, newlines).
    - Think of it as a radar that pings whenever it detects open space in your text.

### **Putting Special Sequences to the Test**

1. **The Digit Hunter in Action**:
    - **Task**: Extract all phone numbers from a text for a phone number in the format 'XXX-XXX-XXXX', where each 'X' is a digit
    - **Regex Pattern**: `\d{3}-\d{3}-\d{4}`
    - **Test Sentence**: "Call me at 123-456-7890 or 987-654-3210."
    - **Expected Matches**: `['123-456-7890', '987-654-3210']`
    - **Explanation**: The `\d` sequence finds digits, and `{3}` specifies exactly three digits. The hyphen `-` is a literal character, It separates different segments of the phone number. Overall, this pattern searches for sequences like a U.S. standard phone number format.
2. **The Word Wizard’s Spell**:
    - **Task**: Identify words containing numbers.
    - **Regex Pattern**: `\w+\d+\w*`
    - **Test Sentence**: "My username is user123 and my password is pass99word. my really cool username is Rhoadehouse10 fhosdhflsjdhfljsdhf"
    - **Expected Matches**: `['user123', 'pass99word', "Rhoadehouse]`
    - **Explanation**: `\w*` matches any word character zero or more times, and `\d` ensures there's at least one digit. This pattern finds words mixed with numbers.
3. **The Space Scout’s Exploration**:
    - **Task**: Split a sentence into words.
    - **Regex Pattern**: `\s+`
    - **Test Sentence**: "Welcome to the world of        regex!"
    - **Expected Matches**: The spaces between ' ', ' ', ' ', ' ', '        '’
    - **Explanation**: `\s+` matches one or more whitespace characters. It does not match the characters of the words themselves but the empty space that separates them, allowing us to see where one-word ends and another begins.

### **More Special Sequences**

1. **\D - The Non-Digit Detector**
    - Finds any character that is not a digit.
    - Like a filter that lets everything but coins pass through.
2. **\W - The Non-Word Character Identifier**
    - Matches any character that is not a word character (opposite of \w).
    - Imagine it as a tool that highlights everything in the text that isn't a word or number.
3. **\S - The Non-Whitespace Finder**
    - Identifies any character that is not a whitespace.
    - It's like a spotlight that ignores spaces and shines on everything else.
4. **\b - The Word Boundary Beacon**
    - A marker for the positions between a word and a non-word character.
    - Think of it as a flare that lights up the borders of each word.
5. **\B - The Non-Word Boundary Signal**
    - Matches positions where a word boundary does not occur.
    - It’s the silent guardian that watches over continuous strings of word characters without interruption.
6. **\A - The Beginning Sentinel**
    - Matches only at the start of the string.
    - It’s like a gatekeeper that only allows patterns that appear right at the opening of your text.
7. **\Z - The End Guardian**
    - Matches only at the end of the string, before the final newline, if one exists.
    - Think of it as the final checkpoint at the very end of your textual journey.

### **Exercises to Master the Art**

1. **Task**: Find non-digit characters in a string.
    - **Regex Pattern**: **`\D+`**
    - **Test Sentence**: "Room 101 is on floor 3"
    - **Expected Matches**: `['Room ', ' is on floor ']`
    - **Explanation**: **`\D+`** matches one or more non-digit characters, capturing the words and spaces in the sentence.
2. **Task**: Identify characters that are not part of words.
    - **Regex Pattern**: **`\W`**
    - **Test Sentence**: "Hello, world! Are you ready?"
    - **Expected Matches**: `[',', ' ', '!', ' ', ' ', ' ', '?']`
    - **Explanation**: **`\W`** finds any character that is not a letter, digit, or underscore, like punctuation and spaces in this case.
3. **Task**: Identify non-whitespace characters in a string.
    - **Regex Pattern**: **`\S`**
    - **Test Sentence**: "Python 3.12 - New Features"
    - **Expected Matches**: Matches each non-space character individually, including letters, numbers, dots, and dashes.`['P', 'y', 't', 'h', 'o', 'n', '3', '.', '1', '2', '-', 'N', 'e', 'w', 'F', 'e', 'a', 't', 'u', 'r', 'e', 's']`
4. **Task**: Find words that start with 'py'.
    - **Regex Pattern**: **`\bPy\w*`**
    - **Test Sentence**: "Python is easy. Typing is fun.Python"
    - **Expected Matches**: `['Python']` from the beginning of the sentence.
    - **Explanation**: **`\b`** ensures the match starts at a word boundary, and **`\w*`** matches any word characters following 'Py'.
5. **Task**: Find instances of 'oo' not at the start or end of a word.
    - **Regex Pattern**: **`\Boo\B`**
    - **Test Sentence**: "The spooky moonlight illuminated the room."
    - **Expected Matches**: 'oo' in 'spooky', 'moonlight', and ‘room’.
    - **Explanation**:**`\B`** is used to find matches where a word boundary does not exist. In this case, it ensures that the pattern 'oo' is not at the start or end of a word. The regex pattern **`\Boo\B`** specifically looks for occurrences of 'oo' where both the preceding and following characters are also word characters (like letters or digits). It ignores cases where 'oo' is at the beginning or end of a word.
6. **Task**: Check if a string starts with 'Hello'.
    - **Regex Pattern**: **`\AHello`**
    - **Test Sentence**: "Hello, welcome to the world of Python! Hello again"
    - **Expected Matches**: `['Hello']` at the very beginning of the string.
    - **Explanation**: **`\AHello`** matches 'Hello' only if it appears at the start of the entire string.
7. **Task**: Match a pattern only if it's at the very end of the string.
    - **Regex Pattern**: **`Python\Z`**
    - **Test Sentence**: "Starting with basics and ending with Python"
    - **Expected Matches**: `['Python']` at the end of the sentence.
    - **Explanation**: **`Python\Z`** finds 'Python' as it's precisely at the end of the string, acting as a concluding marker.



## **Discovering the Power of Sets in Regular Expressions**

Just as a painter mixes colors to create the perfect shade, sets in regex allow you to mix and match characters to 
find exactly what you're looking for in a sea of text. They are your customizable tools, letting you define specific groups of characters to search for. 

- Sets in regex, denoted by square brackets `[]`, let you define a group of characters that you wish to match. 
  It's like selecting specific colors from your palette to create a unique hue.
- They can be as simple as `[abc]`, which matches any one of 'a', 'b', or 'c', or as complex as `[a-z]`, which matches any lowercase letter.

### **Exploring Ranges and Patterns**

- Within sets, you can define ranges. For example, `[a-e]` matches any letter from 'a' to 'e'. It's like choosing a range of colors 
  from blue to green on your palette.
- You can also mix individual characters and ranges, like `[A-Za-z0-9]`, to match any alphanumeric character.

### **Integrating Sets with Python Concepts**

- **With Loops**: Iterate through strings, using sets in regex to process or extract specific patterns.
- **With Conditions**: Use sets in regex within conditional statements to make decisions based on text patterns.

### **Practical Examples and Exercises**

1. **Task**: Find all vowels in a string.
    - **Regex Pattern**: `[aeiou]`
    - **Test Sentence**: "Regular expressions are fun."
    - **Expected Matches**: `['e', 'u', 'a', 'e', 'e', 'i', 'o', 'a', 'e', 'u']`
    - **Explanation**: The set `[aeiou]` matches any vowel in the sentence, picking them out like bright colors on a canvas.
2. **Task**: Identify all uppercase and lowercase letters.
    - **Regex Pattern**: `[A-Za-z]`
    - **Test Sentence**: "Regex in Python 3.12 is powerful!"
    - **Expected Matches**: Each individual letter in the sentence. But no the digits or special characters (!). `['R', 'e', 'g', 'e', 'x', 'i', 'n', 'P', 'y', 't', 'h', 'o', 'n', 'i', 's', 'p', 'o', 'w', 'e', 'r', 'f', 'u', 'l']`
    - **Explanation**: `[A-Za-z]` includes all lowercase and uppercase letters, leaving out numbers and symbols, like selecting only the primary colors from a set.
3. **Task**: Identify all digits and special characters in a string.
    - **Regex Pattern**: `[0-9!@#\$%\^&\*\(\)]`
    - **Test Sentence**: "The price is $15 for 3 items! #Sale"
    - **Expected Matches**: `['$', '1', '5', '3', '!', '#']`
    - **Explanation**: The set `[0-9!@#\$%\^&\*\(\)]` is like selecting both the numbers and special accent colors on your palette, allowing you to pick out digits and special characters from the sentence.
4. **Task**: Find any lowercase letter, exclamation point, or question mark.
    - **Regex Pattern**: `[a-z!?]`
    - **Test Sentence**: "What is regex? It's amazing!"
    - **Expected Matches**: Lowercase letters, '?', '!'. `['h', 'a', 't', 'i', 's', 'r', 'e', 'g', 'e', 'x', '?', 't', 's', 'a', 'm', 'a', 'z', 'i', 'n', 'g', '!']`
    - **Explanation**: `[a-z!?]` combines a range of lowercase letters with '!' and '?', similar to choosing a set of basic colors and adding a couple of bright ones for emphasis.

'''

## Introduction to the `re` Module: Python's Gateway to Regular Expressions

### **Key Features of the `re` Module**
'''
    - **`re.findall()`**: Retrieves all non-overlapping matches of a pattern in a string, returning them as a list.
    - **`re.search()`**: Scans through a string, looking for any location where the pattern matches.
    - **`re.match()`**: Determines if the regex pattern matches at the beginning of a string.
    - **`re.split()`**: Splits a string by occurrences of the pattern.
    - **`re.sub()`**: Replaces occurrences of the pattern in a string with a replacement string.

'''
# Find vowels in a set
print(r"Hello")
import re
text = "Regular expressions are fun."
vowels = re.findall(r"[aeiou]", text)
print(vowels)

# finding capital and lower case letters with a set
text = "Regex in Python 3.12 is powerful!"
letters = re.findall(r"[A-Za-z]", text)
print(letters)

text = "The price is $15 for 3 items! #Sale! :()"
#                       any combination of characters
digits = re.findall(r"[0-9!@#\$%\^&\*\(\)]", text)
print(digits)


text = "Contact us at support@example-place.com or sales@example.test.com or rhoades.webdev@gmail.com"
#                       email name    @    domain      .   com
#                         set1             set2           set3
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-z]{2,}", text)
#                       cooldude_74   @    gmail       .   com
#set 1 any combination of alphanumeric character - capital/lowercase letters - any valid special characters youll find in an email name
# set 2 any combination of alphanumeric character - capital/lowercase letters - dot or hyphen for domain name
# set 3 any capital or lowercase letter betwteen a and z, that occurs at least 2 times 

print(emails)


# searching a twitter post for hashtags
import re
post = "Just hanging out in me swamp with my lady Fiona! #marriedlyfe #watrudoininmeswamp #shrekislove #shrekislife #DON-KEH"
hashtags = re.findall(r"#\w+-?\w*", post)
print(hashtags)


# re.search() - return the first instance of a match
# returns a match object
# example match object
post = "Just hanging out in me swamp with my lady Fiona! #marriedlyfe #watrudoininmeswamp #shrekislove #shrekislife #DON-KEH"
hashtags = re.search(r"#\w+-?\w*", post)
print(hashtags.group()) #<-- part of the string that matches our pattern
# print(hashtags[0])


email = "swampdaddy@exclude.com"
valid_email = re.search(r"[A-Za-z0-9._%+-]+@[yahoo]+\.[A-z]{2,}", email)
print(valid_email)
if valid_email:
    print(valid_email.group())
    print("Valid Email Adress")
else:
    print("Invalid Email")

text = " , swampdaddy@ aol.com "
emails = [email for email in re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text) if 'exclude.com' not in email]
print(emails)

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
print(emails)

# validate phonenumber
text = "Contact us at 123-456-890."
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
print(match)
if match:    
    print(match.group())
    print(match.span())
else:
    print("didnt find a match")

# extracting a year from a date'
special_event = "The very special event was held 15/06/2021"
match = re.search(r"\b\d{4}\b", special_event)
if match:
    print(f"Year extracted: {match.group()}")

special_event = "The very special event was 2024 on 15/06/2021"
years = re.findall(r"\b\d{4}\b", special_event)
print(years)

# re.match()
text = "Hello, world!"
if re.match(r"^Hello", text):
    print("The string starts with Hello!")
else:
    print("The string does not stat with Hello")


# extracting specific pattern from a url
url = "www.swampdaddies.com"
match = re.match(r"^https|http", url)
if match:
    print("Protocol Found: ", match.group())
else:
    print("That website is not secure")


# re.split()
# split a string by a specific pattern into a list of strings
text = "Python,Regex,splitting-Examples. Fun, right cool beans"
words = re.split(r"[,;.\s?-]+", text)
print(words)


sentence = "He_llo, world! Welcome to Regex. It's the Devil."
parts = re.split(r"(\W+)", sentence)
print(parts)

sentence = "He_llo, world! Welcome to Regex. It's the Devil."
parts = re.split(r"[\s!,]", sentence)
print(parts)

# .sub()
# we're format a phone number into only digits
phone = "Phone: +1 (123) 456-7890"
standard_phone = re.sub(r"\D", "", phone)
print(standard_phone)


phone = "hello this is my phone number 12 345 677 89"
standard_phone = re.sub(r"\D", "", phone)
print(standard_phone)

# Cleaning html elements
html = "<p>This is <em>HTML</em> content!</p>"
clean_text = re.sub(r"<.*?>", "", html)
print(clean_text)


# looking for words in a list of strings
def sentiment_tracker(comment):
    positive_pattern = r"\b(thank|love|happy|great|excellent|good)"
    negative_pattern = r"\b(hate|hated|angry|bad|terrible|poor|worst|shitty)"

    try:
        if re.search(positive_pattern, comment, re.IGNORECASE):#ignore case sensitivty
            print(re.search(positive_pattern, comment, re.IGNORECASE).group() )   
            
            return "Positive"
        elif re.search(negative_pattern, comment, re.IGNORECASE):
            print(re.search(negative_pattern, comment, re.IGNORECASE).group()  )
           
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        print(f"Error analyzing comment: {e}")
        return "Neutral"
    
# sample list of comments
comments = [
"It is terrible how much I love this product! Afterward i had a terrible time in the bathroom.",
"Terrible service, I'm angry.",
"Not sure about the quality.",
"Excellent customer support, thank you!",
"Worst experience ever."


]

sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}
for comment in comments:
    sentiment = sentiment_tracker(comment)
    sentiment_count[sentiment] += 1

# Displaying categorized sentiments
for sentiment, count in sentiment_count.items():
    print(f"{sentiment} Comments: {count}")

date_string = "Todays date is 28/03/2024"
#          groups             1      2       3         3  2   1
formatted_date = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3donkeh\2donkey\1", date_string)
print(formatted_date)


"""
Parentheses `()` around \`d{2}` and `\d{4}` create capture groups.
These groups allow us to remember and reference specific parts of the matched text.
In this pattern, there are three capture groups:

- The first **`(\d{2})`** captures the day.
- The second **`(\d{2})`** captures the month.
- The third **`(\d{4})`** captures the year.

The replacement pattern **`r"\3-\2-\1"`** specifies how to format the captured groups in the replacement string.

- **`\3`** refers to the third capture group (the year).
- **`\2`** refers to the second capture group (the month).
- **`\1`** refers to the first capture group (the day).


"""
















