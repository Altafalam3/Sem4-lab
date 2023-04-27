#!/bin/bash

echo "Enter the filename: "
read filename

# Count number of characters
char_count=$(grep -o '.' $filename | wc -l)

# Count number of words
word_count=$(grep -o '\w\+' $filename | wc -l)

# Count number of lines
line_count=$(grep -c '^' $filename)

echo "Number of characters: $char_count"
echo "Number of words: $word_count"
echo "Number of lines: $line_count"
