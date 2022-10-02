newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)
print(len((set(newspaper) | set(magazine)) - set(both)))