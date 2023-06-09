#imports the library
# from selenium import webdriver
import time
 
from dragonfly import (Function, Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Pause)  


class CodeMappings(MappingRule):
    mapping = {
        'close tab': Key('c-w'),
        'open tab': Key('c-t'),
        'restore tab': Key('cs-t'),
        'last tab': Key('cs-t'),
        'book snap': Key('cs-b'),
        'book add': Key('c-d'),
        'tab <tab>': Key('c-%(tab)d'),
        'down <number>': Key('down:%(number)d'),
        'up <number>': Key('up:%(number)d'),
        'down': Key('down'),
        'up': Key('up'),
        'downy': Key('d'),
        'upy': Key('u'),
        'go back': Key('a-left'),
        'go forward': Key('a-right'),
        'load': Key('f5'),
        'snurch': Key('c-l'),
        

        # code - bricks
        'zap': Key('c-slash'), 
        'run me': Key('c-enter'), 
        'run it': Key('s-enter'), 
        'run up': Key('sa-up'), 
        'run down': Key('sa-down'), 
        'nexty': Key('c-pgdown'),
        'previ': Key('c-pgup'),
        'insert up': Key('ca-p'),
        'insert down': Key('ca-n'),
        'split cell': Key('ca-n'),
        'copy cell': Key('ca-c'),
        'cut cell': Key('ca-x'),
        'del cell': Key('ca-d'),
        'del line': Key('s-delete'),
        'cell down': Key('ca-down'),
        'indent me': Key('c-]'),
        'dedent me': Key('c-['),
        'find me': Key('ca-f'),
        'paste wheel': Text('dbfs:/FileStore/jars/passlist-1.0.0-py3-none-any.whl'),
        'print <snaketext>': Text('print(') + Text('%(snaketext)s') + Text('_df.count())'),
        'display <snaketext>': Text('display(') + Text('%(snaketext)s') + Text('_df)'),
        'frame <snaketext>': Text('%(snaketext)s') + Text('_df'),
        'log <snaketext>': Text('print(') + Text('%(snaketext)s') + Text('_df.count())') + Key("enter") + Text('display(') + Text('%(snaketext)s') + Text('_df)'),
        'F call': Text('F.col("")') + Key('left:2'),
        'to select': Text('.select()') + Key('left:1'),
        'to join': Text('.join()') + Key('left:1'),
        'to where': Text('.where()') + Key('left:1'),
        'to distinct': Text('.distinct()'),
        'to column': Text('.withColumn("")') + Key('left:2'),
        # "<lowtext>": Text("%(lowtext)s"),

        

        #snippets
        'magic mark': Key('percent, m, d, enter, #,#'),
        'magic run': Key('percent, r, u, n, space'),
        'con blob': Key('percent, r, u, n, space') + Text(' "../ConnectBlob"'),
        'snip display': Text('display('),
        'snip alias': Text(".alias('')") + Key('left:2'),
        'snip show': Text(".show()"),
        'snip select': Text(".select("),

        #azure
        'Open test': Key("c-t") + Text(R'https://adb-2707707152410749.9.azuredatabricks.net/?o=2707707152410749#job/list') + Key("enter"),
        'Open qa': Key("c-t") + Text(R'https://adb-1477701841953214.14.azuredatabricks.net/?o=1477701841953214#joblist') + Key("enter"),
        'Open prod': Key("c-t") + Text(R'https://adb-8131518869320383.3.azuredatabricks.net/?o=8131518869320383#job/list') + Key("enter"),
        'Open failed': Key("c-t") + Text(R'https://adb-8131518869320383.3.azuredatabricks.net/?o=8131518869320383#job/runs?status=failed&offset=0') + Key("enter"),
    }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 99999),
        Dictation("text"),
        Dictation("pascal_text", default="").title().replace(" ", ""),
        Dictation("lowtext").lower(),
        Dictation("snaketext").lower().replace(" ", "_"),
    ]

context = AppContext(executable='firefox')
grammar=Grammar('Edge',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None