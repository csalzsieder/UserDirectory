#imports the library
import os
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mimic)

def foo(slot):
    t = int(slot)
    x = .15
    z = .05
    y = (t*z)
    zed = y + x - z
    return "(0.1, {}), left".format(zed)

def bar(test):
    print(test) 

class CodeMappings(MappingRule):
    mapping = {  
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
		'previ': Key('c-pgup'),
		'nexty': Key('c-pgdown'), 
		'Save them': Key('c-k,s'),
		'X open': Key('cs-e'),
		'Text open': Key('cs-g'),
		'Sidebar': Key('c-b'),
		'Reload browser': Key('w-4') + Pause('50') + Key('f5') + Pause('50') + Key('w-5'),
		'Goat ref': Key('sa-f12'),
        'select line <number>': Key('c-g') + Text('%(number)d') + Key('enter,s-end,c-c'),
        'line <number>': Key('c-g') + Text('%(number)d') + Key('enter,end'),
        'line comment': Key("c-k,c-c"),
        'line uncomment': Key("c-k,c-u"),
        'tab <tab>': Key('a-%(tab)d'),
        'get check out develop': Key("c-`,") + Pause("20") + Text("git co develop") + Key("enter"),
        'get check out feature': Key("c-`,") + Pause("20") + Text("git co feature/DF-"),
        'get called release': Key("c-`,") + Text("git cob release/"),
        'get called feature': Key("c-`,") + Text("git cob feature/DF-"),
        'num var': Key("%,(,n,u,m,b,e,r,),d"),
        'git checkout <text>': Key("c-`") + Text("git co %(text)s/"),
        'yarn run <text>': Key("c-k, s, c-`") + Pause('10') + Text("yarn run %(text)s") + Key("enter"), #build, dev
        'yarn <text>': Key("c-k, s, c-`") + Pause('10') + Text("yarn %(text)s") + Key("enter"), #install, lint, clean

        # 'test': bar("text"),  
    }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
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