#imports the library
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from dragonfly import (Function,Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mimic)

def bar():
    # driver.execute_script("window.open('');")
    driver.get('https://python.org')

def start_selenium():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    path = "/Users/csalzsieder/chromedriver_win32/chromedriver"
    driver = webdriver.Chrome(path, chrome_options=options)

class CodeMappings(MappingRule):
    mapping = {  
        # Snippets
        'text snip': Text('text') + Pause('50') + Key('tab'),
        'key snip': Text('key') + Pause('50') + Key('tab'),
        'pause snip': Text('pau') + Pause('50') + Key('tab'),
        'pie def': Text('df'),
        'in com': Text('# COMMAND ----------'),

        # Python
        'py com': Text('##############################') + Key('enter') + Text('# '),
        'py com end': Text('##############################') + Key('enter'),

        # debugging
        'run it': Key("f5"),
        'kill it': Key("s-f5"),
        'restart': Key("cs-f5"),
        'step in': Key('f11'),
        'step over': Key('f10'),
        'step out': Key("s-f11"),
        'breaks snap': Key("f9"),

        # open files
        "Open pie": Key("c-k,c-o,a-d") + Pause('50') + Text(R'C:\NatLink\NatLink\MacroSystem') + Key("enter:2"),
        "Open react": Key("c-k,c-o,a-d") + Pause('50') + Text(R"D:\GitProjects\react-components") + Key("enter:2"),
        "Open code": Key("c-k,c-o,a-d") + Pause('50') + Text(R"D:\GitProjects") + Key("enter:2"),

        # Editing
        'replace local': Key("c-h"),
		'replace global': Key("cs-h"),
        'back space': Key('backspace'),
        'Div <text>': Text('<div>%(text)s</div>'),
        'Open folder': Key('c-k,c-o'),
        'New copy': Key('c-c,c-v'),
        'copy down': Key('sa-down'),
		'Load web': Key('w-4') + Pause('50') + Key('f5') + Pause('50') + Key('w-5'),
        'copy line <number>': Key('c-g') + Text('%(number)d') + Key('enter,s-end,c-c'),
        'select line <number>': Key('c-g') + Text('%(number)d') + Key('enter,s-end'),
        'select multi <number>': Key("shift:down, ctrl:down, alt:down, down:%(number)d, shift:up, ctrl:up, alt:up,"),
        # 'line <number>': Key('c-g') + Pause('5') + Text('%(number)d'),
        'line <number>': Key('c-g') + Text('%(number)d') + Key('enter,end'),
        # 'line <number> <n>': Key('c-g') + Text('%(number)d') + Key('enter,end') + Key('left:%(n)d'),
        'oink': Key("c-k,c-c"),
        'meow': Key("c-k,c-u"),
        'del line': Key("s-delete"),
        'tab <tab>': Key('a-%(tab)d'),
        'Change language': Key('c-k,m'),

        # Navigation
        'snurch': Key('cs-f'),
        'previ': Key('c-pgup'),
        'nexty': Key('c-pgdown'), 
        'Save all': Key('c-k,s'),
        'Save': Key('c-s'),
        'see view': Key('cs-e'),
        'team view': Key('cs-g,g'),
        'term view': Key('csa-t'),
        'Open tab': Key('c-n'),
        'Sidebar': Key('c-b'),
        'find death': Key('sa-f12'),
        'goat death': Key('f12'),
        'Goat': Key('c-p'),
        'Goat funk': Key('cs-o'),
        'Goat prop': Key('cs-p'),
        'focus code': Key('c-j'),
        'close all': Key('c-k,w'),
        'close tab': Key('c-f4'),
        'key cuts': Key('c-k, c-s'),
        'rename': Key('f2'),
        'doneUnder': Text('__'),
        # '<nocaps>': Text('%(noccaps)s'),
        # Commands
        'Execute <text>': Key('cs-p') + Text('Execute %(text)s') + Key('enter'), #Query, selected

        # git 
        'get check out develop': Key('csa-t') + Text('inter') + Key('enter') + Pause("20") + Text("git co develop && git pull") + Key("enter"),
        'get check out feature': Key('csa-t') + Pause("20") + Text("git co feature/"),
        'get called release': Key('csa-t') + Text("git cob release/"),
        'get called feature': Key('csa-t') + Text("git cob feature/DF-"),
        'num var': Key("%,(,n,u,m,b,e,r,),d"),
        'get checkout <text>': Key('csa-t') + Text("git co %(text)s/"),
        'get merge <text>': Key('csa-t') + Pause("20") + Text("git merge --%(text)s"), #Continue, abort
        'get merge develop': Key('csa-t') + Text("git merge origin/develop") + Key('enter'),
        'get commit': Key('csa-t') + Pause("10") + Text('git commit -am ""') + Pause("10") +         Key('left'),
        'get push': Key('csa-t') + Pause("10") + Text('git push') + Pause("10") + Key('enter'),
        'get pull': Key('csa-t') + Pause("10") + Text('git pull') + Pause("10") + Key('enter'),
        'get branch': Key('csa-t') + Pause("10") + Text('git branch -r') + Pause("10") + Key('enter'),

        # Builds
        'yarn <text>': Key('csa-t') + Pause('10') + Text("yarn %(text)s") + Key("enter"), #install, lint, clean, build, dev
        'build wheel': Key('csa-t') + Pause('10') + Text('./buildLoadWheelToCluster.sh') + Key('enter'),

        # 'test': bar("text"),  
    }
    extras=[
        Integer('tab', 1, 20),
        Integer('number', 1, 9999),
        Integer('n', 1, 9999),
        Dictation("text"),
        Dictation("nocaps", default="").lower(),
        Dictation("camel_text", default="").camel(),
        Dictation("snaketext", default="").lower().replace(" ", "_"),
    ]

context = AppContext(executable='code')
grammar=Grammar('Visual Studio Code',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None