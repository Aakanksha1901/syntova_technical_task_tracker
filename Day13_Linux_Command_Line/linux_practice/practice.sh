
#!/bin/bash

# DAY 13: Linux Command Line Practice

echo "Welcome to Linux Command Line Practice"

USER_NAME="Candidate"
echo "Hello, $USER_NAME"

if [ -f "sample.txt" ]; then
    echo "sample.txt exists"
else
    echo "sample.txt was not found"
fi

echo "Displaying sample file lines:"

for number in 1 2 3
do
    echo "Practice number: $number"
done

echo "Total lines in sample.txt:"
wc -l < sample.txt

echo "Linux practice completed"
