
# DAY 13: Linux Command Line

## Objective
Learn basic to intermediate Linux commands for managing files,
searching text, checking permissions, and running shell scripts.

## 1. Navigation Commands
- `pwd` - Displays the current directory.
- `ls` - Lists files and folders.
- `ls -la` - Lists all files, including hidden files.
- `cd` - Changes the current directory.
- `cd ..` - Moves to the parent directory.

## 2. File and Directory Commands
- `mkdir` - Creates a directory.
- `touch` - Creates an empty file.
- `cp` - Copies a file.
- `mv` - Moves or renames a file.
- `rm` - Removes a file.
- `rmdir` - Removes an empty directory.
- `cat` - Displays file contents.
- `head` - Displays the first lines of a file.
- `tail` - Displays the last lines of a file.

## 3. Search and Text Processing
- `find` - Searches for files and directories.
- `grep` - Searches for matching text.
- `wc` - Counts lines, words, and characters.
- `sort` - Sorts lines.
- `cut` - Extracts selected fields.
- `awk` - Processes structured text.
- `|` - Passes output from one command to another.
- `>` - Writes output to a file, replacing its contents.
- `>>` - Appends output to a file.

## 4. Permissions
- `ls -l` - Displays file permission information.
- `chmod` - Changes file permissions.
- `r` - Read permission.
- `w` - Write permission.
- `x` - Execute permission.

## 5. System and Process Commands
- `whoami` - Displays the current username.
- `date` - Displays the current date and time.
- `uname -a` - Displays system information.
- `df -h` - Displays disk space information.
- `du -sh` - Displays the size of a directory.
- `ps` - Lists processes.
- `top` - Displays running processes.
- `echo $HOME` - Displays the home directory.
- `echo $PATH` - Displays executable search paths.

## 6. Shell Scripting
- A shell script stores commands in a file.
- `#!/bin/bash` specifies Bash as the interpreter.
- Variables store values for reuse.
- `if` statements execute commands based on conditions.
- `for` loops repeat commands.
- `bash practice.sh` runs the script.
- `bash -n practice.sh` checks script syntax.

## 7. Practical Work Completed
- Created directories and text files.
- Copied and renamed files.
- Displayed and searched file contents.
- Used line and word counting commands.
- Practised permissions and system information.
- Created and executed a Bash script.

## Note
The practical was performed using Git Bash on Windows.
Git Bash provides many Unix-style commands but is not a native Linux OS.
