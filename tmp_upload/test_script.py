import paramiko

path = "C:/Users/Dell/Desktop/tourism/tmp_upload/HeroSection_original.tsx"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

print("Read", len(content), "chars")
print("Done")
