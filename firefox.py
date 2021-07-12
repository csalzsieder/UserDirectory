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
        'line nip': Key('c-slash'), 
        'run me': Key('c-enter'), 
        'run it': Key('s-enter'), 
        'run up': Key('sa-up'), 
        'run down': Key('sa-down'), 
        'nexty': Key('c-pgdown'),
        'previ': Key('c-pgup'),
        'insert up': Key('ca-p'),
        'insert down': Key('ca-n'),
        'insert display': Key('ca-p') + Pause('100') + Text('display('),
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
        

        #snippets
        'magic mark': Key('percent, m, d, space, #,#'),
        'magic run': Key('percent, r, u, n, space'),
        'con blob': Key('percent, r, u, n, space') + Text(' "../ConnectBlob"'),
        'snip display': Text('display('),
        'snip alias': Text(".alias('')") + Key('left:2'),
        'snip show': Text(".show()"),
        'snip select': Text(".select("),

        #azure
        'Open bricks': Key("c-t") + Text(R'https://adb-1477701841953214.14.azuredatabricks.net/?o=1477701841953214#joblist') + Key("enter"),
    }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 99999),
        Dictation("text"),
        Dictation("pascal_text", default="").title().replace(" ", ""),
    ]

context = AppContext(executable='firefox')
grammar=Grammar('Edge',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None