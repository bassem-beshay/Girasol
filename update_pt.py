import paramiko
import sys

HOST = "50.6.250.81"
USER = "bassem"
PASS = "852456312002Bassem**"
FILE = "/home/bassem/Girasol/frontend/src/components/home/PopularTours.tsx"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PASS)
print("Connected to server")
ssh.close()
