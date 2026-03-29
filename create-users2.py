#!/usr/bin/python3

# INET4031
# Chali Xiong
# 3/29/2026
# 3/29/2026

import os
import re

def main():
    # Ask the user if they want dry-run mode
    dry_run = None
    while dry_run not in ("Y", "N"):
        dry_run = input("Run in dry-run mode? (Y/N): ").strip().upper()

    # Open the input file and process each line
    with open("create-users.input") as f:
        for line in f:
            line = line.strip()

            # Skip comments or invalid lines
            if line.startswith("#") or len(line.split(':')) != 5:
                continue

            # Extract user info
            fields = line.split(':')
            username = fields[0]
            password = fields[1]
            gecos = "%s %s,,," % (fields[3], fields[2])
            groups = fields[4].split(',')

            # Create user account
            print(f"==> Creating account for {username}...")
            if dry_run == "N":
                cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
                os.system(cmd)

            # Set password
            print(f"==> Setting the password for {username}...")
            if dry_run == "N":
                cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
                os.system(cmd)

            # Assign to groups
            for group in groups:
                if group != '-':
                    print(f"==> Assigning {username} to the {group} group...")
                    if dry_run == "N":
                        cmd = f"/usr/sbin/adduser {username} {group}"
                        os.system(cmd)

if __name__ == '__main__':
    main()
