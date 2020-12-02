file_url = "input"
passwords = []
with open(file_url, 'r') as f:
    for line in f:
        passwords.append(line)

pass_count = 0

for password in passwords:
    pass_split = password.replace("\n", '').split(" ")
    password = str(pass_split[2])
    letter_to_find = str(pass_split[1].replace(":", ''))
    indices = pass_split[0].split("-")
    index_1 = int(indices[0])
    index_2 = int(indices[1])
    if (password[index_1-1] == letter_to_find) ^ (password[index_2-1] == letter_to_find):
        pass_count += 1

print(pass_count)