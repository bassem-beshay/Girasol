import paramiko, sys
sys.stdout.reconfigure(encoding="utf-8")

with open("C:/Users/Dell/Desktop/tourism/Footer_original.tsx", "r", encoding="utf-8") as f:
    c = f.read()
print(f"Read {len(c)} chars")

# All replacements as (old, new) tuples
replacements = []
