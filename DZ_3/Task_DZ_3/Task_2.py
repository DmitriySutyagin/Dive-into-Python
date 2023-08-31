# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.


# help()


text = '''Welcome to Python 3.11's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.11/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".
'''
new_text = text.replace('/', ' ').replace(',', ' ').replace('.', ' ').replace('"', ' ').replace('!', ' ') \
    .replace(':', ' ').replace(';', ' ').replace('-', ' ').replace("'", ' ').lower().split()
print(new_text)
print()
d = {i: new_text.count(i) for i in new_text}
print(dict(sorted(dict.items(d), key=lambda x: x[1], reverse=True)[:10]))