#!/usr/bin/python3

# INET4031
# Chali Xiong
# 3/29/2026
# 3/29/2026

# os is used for system commands. re is used for pattern matching. sys is used for reading input
import os
import re
import sys



def main():
    for line in sys.stdin:

        #This is checking if the lines starts with a "#" 
        #This character is used for comments and are not actual user data.
        match = re.match("^#",line)

        #This will separate the line using a ":" for user info from the input
        fields = line.strip().split(':')

        #This checks if the line is a comment or is not equal to the length of 5
        #If true, the line is skipped
        #It check for "match" which are comments
        #It checks if the data is formmated correctly
        if match or len(fields) != 5:
            continue

        #This assigns values based on the input
        #Also matches format
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #Splits the group by commas 
        groups = fields[4].split(',')

        #Shows that the account is being created
        print("==> Creating account for %s..." % (username))
        #
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #print(cmd)
        #os.system(cmd)

        #Shows that the password is being set for the user
        print("==> Setting the password for %s..." % (username))
        
        #A command to set the password for the user using the passwd command
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print(cmd)
        #os.system(cmd)

        for group in groups:
            #Checks if the group is an actual group. Then add the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
                #os.system(cmd)

if __name__ == '__main__':
    main()
