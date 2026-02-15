import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("50.6.250.81", username="bassem", password="852456312002Bassem**")

print("=== Processing HeroSection.tsx ===")
stdin, stdout, stderr = ssh.exec_command("cat /home/bassem/Girasol/frontend/src/components/home/HeroSection.tsx")
c = stdout.read().decode("utf-8")

