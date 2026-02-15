import paramiko

H = "50.6.250.81"
U = "bassem"
P = "852456312002Bassem**"
F = "/home/bassem/Girasol/frontend/src/components/home/PopularTours.tsx"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(H, username=U, password=P)

si, so, se = ssh.exec_command("cat " + F)
c = so.read().decode()
print(f"Read {len(c)} bytes")
Q=chr(39)
NL=chr(10)
i1="import { useInView } from "+Q+"@/hooks/useInView"+Q+";"
i2=i1+NL+"import { useLanguageStore } from "+Q+"@/store/languageStore"+Q+";"+NL+"import { popularToursT, t } from "+Q+"@/lib/translations"+Q+";"
c=c.replace(i1,i2)
x=1
h1="const [ref, isInView]"
