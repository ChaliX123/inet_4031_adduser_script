# inet_4031_adduser_script

# Program Description
This script automates the process of creating users by reading a list of users from a file and performing the same commands automatically. It creates user accounts, sets passwords, and assigns users to groups based on the input file. The program saves time, reduces human error, and ensures that all accounts are created consistently.

# Program User Operation
This program processes an input file line by line, creating users, setting their passwords, and adding them to groups. The user does not need to manually type each Linux command; instead, the script executes the commands automatically.


# Input File Format
Each line in the input file should have five fields separated by colons. username:password:last_name:first_name:groups

# Command Excuction
- Make sure the script is executable: chmod +x create-users.py
- Run the script with the input file using input redirection: ./create-users.py < create-users.input

# "Dry Run"
A “dry run” is when the script prints all the commands it would execute without actually making any changes to the system. os.system(cmd) lines are commented out, so no users or groups are created.
