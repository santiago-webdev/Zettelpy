#!/usr/bin/env bash

# Check if the program can start
echo "Create directories with the first instance of the program"
zettelpy
if [[ $? -eq 0 ]]; then
    echo "Pass"
fi
sleep 5

# Create a note with a title
echo "Create a note with a title"
zettelpy Test1.md
if [[ $? -eq 0 ]]; then
    echo "Pass"
fi
sleep 5

# Create a note with a title inside a subdirectory
echo "Try creating subdirectories"
zettelpy Testing/Test2.md
if [[ $? -eq 0 ]]; then
    echo "Pass"
fi
sleep 5

# Test the creating of the index
echo "You should only see the index, and after quitting it you should not see another note"
zettelpy -i Test1.md  # The "Test1.md" should be ignored when parsed a -i
if [[ $? -eq 0 ]]; then
    echo "Pass"
fi
sleep 5

# This test is for seeing how the program reacts when parsing a note that
# doesn't exists, and catch the error before it reaches the program to view
zettelpy -v Test853.md  # Should fail beacuse it doesn't exists
if [[ $? -eq 1 ]]; then
    echo "Pass"
fi
sleep 5

# This test is for viewing a note that exists
zettelpy Testing/Test2.md -v
if [[ $? -eq 0 ]]; then
    echo "Pass"
fi
