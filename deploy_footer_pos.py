import paramiko, sys
sys.stdout.reconfigure(encoding='utf-8')

HOST = '50.6.250.81'
USER = 'bassem'
PASS = '852456312002Bassem**'
FILE_PATH = '/home/bassem/Girasol/frontend/src/components/layout/Footer.tsx'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PASS)
print("Connected to server")

sftp = ssh.open_sftp()
with sftp.open(FILE_PATH, 'r') as f:
    content = f.read().decode('utf-8')

# Change from justify-between (far left + far right) to gap layout
# Copyright stays left, Terms moves toward center-right using margin
old = '''<div className="flex flex-col sm:flex-row items-center justify-between gap-3 text-sm text-white/70">'''
new = '''<div className="flex flex-col sm:flex-row items-center gap-3 text-sm text-white/70">'''

if old in content:
    content = content.replace(old, new)
    print("1. Changed container to flex without justify-between")
else:
    print("WARNING: Could not find container div")

# Add sm:ml-auto and sm:mr-[15%] to the terms div to push it toward center-right
old_terms = '<div className="flex items-center gap-6 order-1 sm:order-2">'
new_terms = '<div className="flex items-center gap-6 order-1 sm:order-2 sm:ml-auto sm:mr-[10%]">'

if old_terms in content:
    content = content.replace(old_terms, new_terms)
    print("2. Moved Terms toward center-right")
else:
    print("WARNING: Could not find terms div")

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
