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
    min_and_max = pass_split[0].split("-")
    min_letters = int(min_and_max[0])
    max_letters = int(min_and_max[1])
    num_letters = password.count(letter_to_find)
    if (num_letters <= max_letters) and (num_letters >= min_letters):
        pass_count += 1

print(pass_count)