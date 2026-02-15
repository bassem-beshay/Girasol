import re

path = "/home/bassem/Girasol/frontend/src/components/home/HeroSection.tsx"
with open(path, "r") as fh:
    c = fh.read()

old_imp = "import { contactApi } from "'"@/lib/api"'";"
