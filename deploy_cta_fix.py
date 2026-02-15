import paramiko, sys
sys.stdout.reconfigure(encoding='utf-8')

HOST = '50.6.250.81'
USER = 'bassem'
PASS = '852456312002Bassem**'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PASS)
print("Connected to server")
sftp = ssh.open_sftp()

BASE = '/home/bassem/Girasol/frontend/src/app'

# Target style: like homepage Newsletter
# bg-gradient-to-r from-gray-700 via-gray-600 to-gray-700 rounded-3xl
# With container-custom wrapper and margin bottom for footer separation

changes = {
    'blog/page.tsx': {
        'old': '<section className="py-20 mb-12 bg-gray-900">',
        'new': '<section className="py-12 sm:py-16 md:py-20 mx-4 lg:mx-16 mb-16 bg-gradient-to-r from-gray-700 via-gray-600 to-gray-700 rounded-3xl">',
    },
    'about/page.tsx': {
        'old': '<section className="py-20 mb-12 bg-gray-900">',
        'new': '<section className="py-12 sm:py-16 md:py-20 mx-4 lg:mx-16 mb-16 bg-gradient-to-r from-gray-700 via-gray-600 to-gray-700 rounded-3xl">',
    },
    'destinations/page.tsx': {
        'old': '<section className="py-12 sm:py-16 md:py-20 mb-12 bg-gray-900">',
        'new': '<section className="py-12 sm:py-16 md:py-20 mx-4 lg:mx-16 mb-16 bg-gradient-to-r from-gray-700 via-gray-600 to-gray-700 rounded-3xl">',
    },
    'contact/page.tsx': {
        'old': '<section className="py-20 bg-gradient-to-r from-gray-900 via-gray-800 to-gray-900 mx-4 lg:mx-16 mb-16 rounded-2xl">',
        'new': '<section className="py-12 sm:py-16 md:py-20 mx-4 lg:mx-16 mb-16 bg-gradient-to-r from-gray-700 via-gray-600 to-gray-700 rounded-3xl">',
    },
}

for page, change in changes.items():
    path = f'{BASE}/{page}'
    with sftp.open(path, 'r') as f:
        content = f.read().decode('utf-8')

    if change['old'] in content:
        content = content.replace(change['old'], change['new'])
        with sftp.open(path, 'w') as f:
            f.write(content.encode('utf-8'))
        print(f"Updated {page}")
    else:
        # Try to find the CTA section
        if change['new'] in content:
            print(f"SKIP {page} - already updated")
        else:
            print(f"WARNING {page} - could not find CTA section")
            # Print lines with 'CTA' or 'section' for debugging
            for i, line in enumerate(content.split('\n')):
                if 'CTA' in line or ('bg-gray-900' in line) or ('bg-gradient' in line and 'section' in content.split('\n')[max(0,i-1)].lower()):
                    print(f"  Line {i+1}: {line.strip()}")

sftp.close()

# Build and restart
print("\nRebuilding frontend...")
stdin, stdout, stderr = ssh.exec_command(
    'cd /home/bassem/Girasol/frontend && rm -rf .next && npm run build',
    timeout=300
)
for line in stdout:
    line = line.strip()
    if line:
        try:
            print(line)
        except:
            pass

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
