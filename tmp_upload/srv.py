import os
base = "/home/bassem/Girasol/frontend/src/components/home"
print("Processing HeroSection.tsx")
with open(os.path.join(base, "HeroSection.tsx"), "r") as fh:
    c = fh.read()

# Add imports
old_i = "import { contactApi } from " + chr(39) + "@/lib/api" + chr(39) + ";"
new_i = old_i + chr(10) + "import { useLanguageStore } from " + chr(39) + "@/store/languageStore" + chr(39) + ";" + chr(10) + "import { heroT, t } from " + chr(39) + "@/lib/translations" + chr(39) + ";"
c = c.replace(old_i, new_i)
