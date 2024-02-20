import csv

file_path = 'pokemon.csv'

# initiate variables
total_hp = 0
total_attack = 0
pokemon_count = 0
longest_pokemon_name = ''


with open(file_path, mode = 'r', encoding = 'utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # increment the total HP
        total_hp += int(row['HP'])

        # increment total attack
        total_attack += int(row['Attack'])
        pokemon_count += 1

        # check and update the longest name
        if (len(row['Name']) > len(longest_pokemon_name)):
            longest_pokemon_name = row['Name']

# calculate the average attack
    average_attack = total_attack / pokemon_count if pokemon_count else 0

# print the result
    print(f"Sum of all HP stats: {total_hp}")
    print(f"total count : {pokemon_count}")
    print(f"total attack: {total_attack}")
    print(f"average attack : {average_attack}")
    print(f"longest name: {longest_pokemon_name}")

# a if condition else b，意味着如果condition条件为真，则表达式的结果为a，否则为b。

# f 表示这是一个格式化字符串。如果total_hp的值是12345，print(f"Sum of all HP stats: {total_hp}")就会打印出Sum of all HP stats: 12345。