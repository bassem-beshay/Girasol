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

old_block = """            <div className="flex flex-col sm:flex-row items-center justify-center gap-3 sm:gap-8 text-sm text-white/70">
              <p>
                © {new Date().getFullYear()} Girasol Egypt Travel and Tours. All rights reserved.
              </p>
              <div className="flex items-center gap-6">
                <Link href="/terms" className="hover:text-white transition-colors">
                  Terms & Conditions
                </Link>
                <span className="text-white/30">|</span>
                <Link href="/privacy" className="hover:text-white transition-colors">
                  Privacy Policy
                </Link>
              </div>
            </div>"""

new_block = """            <div className="flex flex-col sm:flex-row items-center justify-between gap-3 text-sm text-white/70">
              <p className="order-2 sm:order-1">
                © {new Date().getFullYear()} Girasol Egypt Travel and Tours. All rights reserved.
              </p>
              <div className="flex items-center gap-6 order-1 sm:order-2">
                <Link href="/terms" className="hover:text-white transition-colors">
                  Terms & Conditions
                </Link>
                <span className="text-white/30">|</span>
                <Link href="/privacy" className="hover:text-white transition-colors">
                  Privacy Policy
                </Link>
              </div>
              <p className="order-3 text-white/50">
                Designed by <a href="tel:+201228986508" className="text-white/70 hover:text-white transition-colors">ENG-Bassem Beshay</a>
              </p>
            </div>"""

if old_block in content:
    content = content.replace(old_block, new_block)
    print("Updated bottom bar layout")
else:
    print("WARNING: Could not find bottom bar block")

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
