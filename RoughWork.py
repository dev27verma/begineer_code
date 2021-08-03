string = "why why why"

for i in range(len(string)):
    if len(string) == 0:
        break
    ch = string[0]
    if i == " " or i == "\t":
        continue
    count = 1
    for j in range(1, len(string)):
        if ch == string[j]:
            count += 1
    string = string.replace(ch, ' ').strip()
    print(f"{ch} -> {count}")
