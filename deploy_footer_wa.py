import paramiko, sys
sys.stdout.reconfigure(encoding='utf-8')

HOST = '50.6.250.81'
USER = 'bassem'
PASS = '852456312002Bassem**'
FILE_PATH = '/home/bassem/Girasol/frontend/src/components/layout/Footer.tsx'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_key_policy = None
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PASS)
print("Connected to server")

sftp = ssh.open_sftp()
with sftp.open(FILE_PATH, 'r') as f:
    content = f.read().decode('utf-8')

old = 'Designed by <a href="tel:+201228986508" className="text-white/90 hover:text-white transition-colors">ENG-Bassem Beshay</a>'
new = 'Designed by <a href="https://wa.me/201228986508" target="_blank" rel="noopener noreferrer" className="underline text-white/90 hover:text-white transition-colors">ENG-Bassem Beshay</a>'

if old in content:
    content = content.replace(old, new)
    print("Updated: underline + WhatsApp link")
else:
    print("WARNING: Could not find the link")

with sftp.open(FILE_PATH, 'w') as f:
    f.write(content.encode('utf-8'))
print("File updated")
sftp.close()

print("\nRebuilding frontend...")
stdin, stdout, stderr = ssh.exec_command(
    'cd /home/bassem/Girasol/frontend && rm -rf .next && npm run build',
    timeout=300
)
for line in stdout:
    line = line.strip()
    if line:
        try: print(line)
        except: pass

exit_code = stdout.channel.recv_exit_status()
print(f"\nBuild exit code: {exit_code}")

if exit_code == 0:
    print("Restarting pm2...")
    stdin, stdout, stderr = ssh.exec_command('pm2 restart all')
    stdout.channel.recv_exit_status()
    print("PM2 restarted successfully!")
else:
    err = stderr.read().decode('utf-8', errors='replace')
    print(f"Build failed! Error:\n{err}")

ssh.close()
print("Done!")
