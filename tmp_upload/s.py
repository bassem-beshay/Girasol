import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("50.6.250.81", username="bassem", password="852456312002Bassem**")

# Upload transform script to server and run it
sftp = ssh.open_sftp()
sftp.put("C:/Users/Dell/Desktop/tourism/tmp_upload/server_transform.py", "/home/bassem/Girasol/server_transform.py")
sftp.close()
stdin, stdout, stderr = ssh.exec_command("python3 /home/bassem/Girasol/server_transform.py")
print(stdout.read().decode())
err = stderr.read().decode()
if err: print("STDERR:", err)
ssh.close()
