# Function A- O(n) space. Is a Reverse String. String slicing (s[::-1]) creates and returns a brand-new string of length n in memory. 
def reverse_string(s):
    return s[::-1]

# Function B- O(n) The counts dictionary stores a new key-value entry for each distinct character in the text, growing linearly with the number of unique characters up to n.
def count_letters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


# Function C- O(n²) space.  It builds an n x n 2D list (matrix), storing n² total integers in memory.
def matrix_identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


# Function D- O(1) space. It only uses a single variable (total) to keep a running sum, requiring constant extra memory regardless of the list size.
def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)

"""Part 2- Trade off decision"""

# Approach 1: Set Approach
# Time Complexity:  O(n) - Single pass to insert and check lookups in O(1) average time.
# Space Complexity: O(n) - Stores all n emails in memory, with higher hash table overhead (~100-150 bytes/item).

def find_duplicates_set(emails):
    seen = set()
    duplicates = set()
    
    for email in emails:
        if email in seen:
            duplicates.add(email)
        else:
            seen.add(email)
            
    return duplicates



# Approach 2: Sort-and-Scan Approach
# Time Complexity:  O(n log n) - TimSort takes O(n log n) time, followed by an O(n) scan.
# Space Complexity: O(n) - Stores all n emails in a list, but with lower per-item memory overhead (~8 bytes/pointer + string objects).

def find_duplicates_sort(emails):
    emails.sort()  # Sorts in-place
    duplicates = set()
    
    for i in range(1, len(emails)):
        if emails[i] == emails[i - 1]:
            duplicates.add(emails[i])
            
    return duplicates


# Function B- O(n) The counts dictionary stores a new key-value entry for each distinct character in the text, growing linearly with the number of unique characters up to n.
def count_letters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


# Function C- O(n²) space.  It builds an n x n 2D list (matrix), storing n² total integers in memory.
def matrix_identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


# Function D- O(1) space. It only uses a single variable (total) to keep a running sum, requiring constant extra memory regardless of the list size.
def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)

"""Part 2- Trade off decision"""

# Approach 1: Set Approach
# Time Complexity:  O(n) - Single pass to insert and check lookups in O(1) average time.
# Space Complexity: O(n) - Stores all n emails in memory, with higher hash table overhead (~100-150 bytes/item).

def find_duplicates_set(emails):
    seen = set()
    duplicates = set()
    
    for email in emails:
        if email in seen:
            duplicates.add(email)
        else:
            seen.add(email)
            
    return duplicates



# Approach 2: Sort-and-Scan Approach
# Time Complexity:  O(n log n) - TimSort takes O(n log n) time, followed by an O(n) scan.
# Space Complexity: O(n) - Stores all n emails in a list, but with lower per-item memory overhead (~8 bytes/pointer + string objects).

def find_duplicates_sort(emails):
    emails.sort()  # Sorts in-place
    duplicates = set()
    
    for i in range(1, len(emails)):
        if emails[i] == emails[i - 1]:
            duplicates.add(emails[i])
            
    return duplicates

