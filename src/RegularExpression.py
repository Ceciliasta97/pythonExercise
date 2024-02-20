import re

with open('/cs/studres/CS2006/Lectures/Python/data/JaneAusten.txt', 'r') as file:
    content = file.read()
# print(content)
    
# all words that begin with the letter ‘y’.
    
words_start_with_y = re.findall(r'\by[a-zA-Z]*', content, re.IGNORECASE)
print(words_start_with_y)


# • the number of occurrences of the word ‘heather’ (use re.IGNORECASE to make count case-
# insensitive)
heather_count = len(re.findall(r'\bheather\b', content, re.IGNORECASE))
print(heather_count)


# • every occurrence of the word ‘heather’ (case-insensitive), along with the word that follows it
heather_follow_by = re.findall(r'\bheather\b\s+(\W+)', content, re.IGNORECASE)
print(heather_follow_by)


# • every occurrence of the word ‘son’, along with the word that follows it
son_follow_by = re.findall(r'\bson\b\s+(\W+)', content, re.IGNORECASE)
print(son_follow_by)

# \s+：匹配一个或多个空白字符。确保"son"和后面的单词之间至少有一些空间（如空格、制表符或换行符）

# (\w+)：这是一个捕获组，匹配一个或多个单词字符。\w是一个字符类，匹配任何字母、数字或下划线，
# 等同于[a-zA-Z0-9_]。+量词表示"一个或多个"前面的元素，因此\w+匹配一个或多个单词字符，捕获一个完整的单词。这部分模式旨在捕获直接跟在"son"后面的单词。