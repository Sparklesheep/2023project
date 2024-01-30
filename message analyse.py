import pandas as pd
import chardet
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open('message.txt', 'r', encoding='utf-8') as file:
    content = file.read()

clean_content = re.sub(r'[^\x00-\x7F]', '', content)

with open('cleaned_message.txt', 'w', encoding='utf-8') as file:
    file.write(clean_content)

with open('cleaned_message.txt', 'r', encoding='utf-8') as file:
    text = file.read()


# 进行单词统计
word_count = {'fix': 0, 'docs': 0, 'perf': 0, 'transition': 0, 'props': 0, 'race condition': 0, 'examples': 0, 'a11y': 0,
              'roles': 0, 'typo': 0, 'GitHub Workflows': 0, 'SvelteKit': 0, 'regression': 0, 'readonly': 0, 'anchor tag': 0}
words = text.split()
for word in words:
    if word.lower() == 'fix':
        word_count['fix'] += 1
    elif word.lower() == 'docs':
        word_count['docs'] += 1
    elif word.lower() == 'perf':
        word_count['perf'] += 1
    elif word.lower() == 'transition':
        word_count['transition'] += 1
    elif word.lower() == 'props':
        word_count['props'] += 1
    elif word.lower() == 'race condition':
        word_count['race condition'] += 1
    elif word.lower() == 'examples':
        word_count['examples'] += 1
    elif word.lower() == 'a11y':
        word_count['a11y'] += 1
    elif word.lower() == 'roles':
        word_count['roles'] += 1
    elif word.lower() == 'typo':
        word_count['typo'] += 1
    elif word.lower() == 'GitHub Workflows':
        word_count['GitHub Workflows'] += 1
    elif word.lower() == 'SvelteKit':
        word_count['SvelteKit'] += 1
    elif word.lower() == 'regression':
        word_count['regression'] += 1
    elif word.lower() == 'readonly':
        word_count['readonly'] += 1
    elif word.lower() == 'anchor tag':
        word_count['anchor tag'] += 1
# 打印结果
print(word_count)

# 创建词云对象
wordcloud = WordCloud(width=800, height=400, background_color='white')

# 生成词云图像
wordcloud.generate_from_frequencies(word_count)

# 绘制词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

labels = list(word_count.keys())
counts = list(word_count.values())
plt.bar(labels, counts)
plt.title("Keyword Counts")
plt.xlabel("Keywords")
plt.ylabel("Counts")
plt.xticks(rotation=45)
plt.show()