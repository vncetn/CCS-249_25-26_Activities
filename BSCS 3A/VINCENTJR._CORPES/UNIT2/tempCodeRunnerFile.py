import re
import nltk
from nltk.corpus import webtext

# ==========================================
# TASK A: Extract words starting with Uppercase
# ==========================================
print("--- TASK A ---")

text_a = """Alice was beginning to get very tired of sitting by her sister on the bank,
and of having nothing to do.  Once or
twice she had peeped into the book her sister was reading, but it had no
pictures or conversations in it, "and what is the use of a book,"
thought Alice, "without pictures or conversations?"""

# Pattern: [A-Z] matches an uppercase letter, \w+ matches the rest of the word
pattern_a = r"[A-Z]\w+"

matches_a = re.findall(pattern_a, text_a)
print("Words starting with uppercase:", matches_a)
print("\n")


# ==========================================
# TASK B: Moby Dick 'Whale' Extraction & Replacement
# ==========================================
print("--- TASK B ---")

# Pattern: Matches Whale, whale, Whales, whales
# [Ww] = W or w
# hale = literal "hale"
# s?   = optional "s" for plural
pattern_b = r"[Ww]hales?"

try:
    # Attempt to read the file
    with open('melville-moby_dick.txt', 'r', encoding='utf-8') as f:
        content_b = f.read()

    # 1. Extract all instances
    whales = re.findall(pattern_b, content_b)
    print(f"Found {len(whales)} instances of 'whale' variations.")

    # 2. Replace the first 10 instances with "leviathan"
    new_content_b = re.sub(pattern_b, "leviathan", content_b, count=10)
    
    # Verification: Print a snippet where changes might have occurred
    print("Replacement complete (first 10 instances).")
    
except FileNotFoundError:
    print("Error: 'melville-moby_dick.txt' not found in the directory.")
    print("Please ensure the file exists to run this part of the code.")

print("\n")


# ==========================================
# TASK C: Jack Sparrow Lines from pirates.txt
# ==========================================
print("--- TASK C ---")

# Ensure NLTK data is downloaded
try:
    nltk.data.find('corpora/webtext')
except LookupError:
    nltk.download('webtext')

# Load content from NLTK
pirates_text = webtext.raw('pirates.txt')

# Pattern:
# ^             = Start of a line
# JACK SPARROW: = Literal name
# (.*)          = Capture group for the dialogue
pattern_c = r"^JACK SPARROW:(.*)"

# re.MULTILINE is required for ^ to match the start of each line, not just the file
jack_lines = re.findall(pattern_c, pirates_text, re.MULTILINE)

print(f"Number of lines spoken by Jack Sparrow: {len(jack_lines)}")
print("First 5 lines:")
for line in jack_lines[:5]:
    print(f" - {line.strip()}")