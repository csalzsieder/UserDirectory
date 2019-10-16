#imports the library
import os
from selenium import webdriver
import time
from dragonfly import (Function,Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mimic)

def foo(slot):
    t = int(slot)
    x = .15
    z = .05
    y = (t*z)
    zed = y + x - z
    return "(0.1, {}), left".format(zed)

def test():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome(executable_path=r"C:\Users\chromedriver.exe")
    print(options)
    driver.get('https://python.org')

class CodeMappings(MappingRule):
    mapping = {  
        'web test': Function(test),
        # Snippets
        'text snip': Text('text') + Pause('50') + Key('tab'),
        'key snip': Text('key') + Pause('50') + Key('tab'),
        'pause snip': Text('pau') + Pause('50') + Key('tab'),

        # open files
        "Open pie": Key("c-k,c-o,a-d") + Pause('50') + Text('C:\NatLink\NatLink\MacroSystem') + Key("enter:2"),
        "Open react": Key("c-k,c-o,a-d") + Pause('50') + Text(R"D:\GitProjects\react-components") + Key("enter:2"),

        # Editing
        'replace local': Key("c-h"),
		'replace global': Key("cs-h"),
        'back space': Key('backspace'),
        'Div <text>': Text('<div>%(text)s</div>'),
        'Open folder': Key('c-k,c-o'),
        'New copy': Key('c-c,c-v'),
        'copy down': Key('sa-down'),
		
		'Load web': Key('w-4') + Pause('50') + Key('f5') + Pause('50') + Key('w-5'),
		
        'select line <number>': Key('c-g') + Text('%(number)d') + Key('enter,s-end,c-c'),
        'line <number>': Key('c-g') + Text('%(number)d') + Key('enter,end'),
        'line <number> <n>': Key('c-g') + Text('%(number)d') + Key('enter,end') + Key('left:%(n)d'),
        'line comment': Key("c-k,c-c"),
        'line uncomment': Key("c-k,c-u"),
        'tab <tab>': Key('a-%(tab)d'),

        # Navigation
        'previ': Key('c-pgup'),
		'nexty': Key('c-pgdown'), 
		'Save them': Key('c-k,s'),
		'X open': Key('cs-e'),
		'Text open': Key('cs-g'),
		'Sidebar': Key('c-b'),
        'find death': Key('sa-f12'),
		'goat death': Key('f12'),
        'Goat': Key('c-p'),
        'focus code': Key('c-j'),

        # git 
        'get check out develop': Key("c-`,") + Pause("20") + Text("git co develop") + Key("enter"),
        'get check out feature': Key("c-`,") + Pause("20") + Text("git co feature/DF-"),
        'get called release': Key("c-`,") + Text("git cob release/"),
        'get called feature': Key("c-`,") + Text("git cob feature/DF-"),
        'num var': Key("%,(,n,u,m,b,e,r,),d"),
        'get checkout <text>': Key("c-`") + Text("git co %(text)s/"),
        'get merge <text>': Key("c-`") + Pause("20") + Text("git merge --%(text)s"), #Continue, abort
        'get merge develop': Key("c-`") + Text("git merge develop") + Key('enter'),
        'get commit': Key("c-`") + Pause("10") + Text('git commit -am ""') + Pause("10") + Key('left'),

        # Builds
        'yarn <text>': Key("c-`") + Pause('10') + Text("yarn %(text)s") + Key("enter"), #install, lint, clean, build, dev

        # 'test': bar("text"),  
    }
    extras=[
        Integer('tab', 1, 20),
        Integer('number', 1, 9999),
        Integer('n', 1, 9999),
        Dictation("text")
    ]

context = AppContext(executable='code')
grammar=Grammar('Visual Studio Code',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None