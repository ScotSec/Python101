from pwn import *
import sys

if len(sys.argv) != 3:
	print("Invalid arguments!")
	print(f">> {sys.argv[0]} <wordlist> <sha256sum>")
	exit()

wanted_hash = sys.argv[2]
password_file = sys.argv[1]
attempts = 0

with log.progress(f"Attempting to crack: {wanted_hash}\n") as p:
	with open(password_file, "r", encoding='latin-1') as password_list:
		for password in password_list:
			password = password.strip("\n").encode('latin-1')
			password_hash = sha256sumhex(password)
			p.status(f"[{attempts}] {password.decode('latin-1')} == {password_hash}")
			if password_hash == wanted_hash:
				p.success(f"Password found! Password = {password.decode('latin-1')} Password hash found after {attempts} attempts! {password.decode('latin-1')} hashes to {wanted_hash}")
				exit()
			attempts += 1
		p.failure("Password hash not found")
