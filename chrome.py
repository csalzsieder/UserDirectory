#imports the library
from selenium import webdriver
import time
 
from dragonfly import (Function, Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Pause)  

def test():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://python.org')
    

def foo():
    print(test)

class GlobalChromeMappings(MappingRule):
    mapping = {
        'web test': Function(test),
        'print test': Function(foo),
        'close tab': Key('c-w'),
        'open tab': Key('c-t, f6:3') + Pause('30') + Key('cs-.'),
        'restore tab': Key('cs-t'),
        'duplicate tab': Key('y/25,t'),                  # vimium
        'last tab': Key('cs-t'),
        'book snap': Key('cs-b'),
        'book add': Key('c-d'),
        'nexty': Key('c-pgdown'),
        'previ': Key('c-pgup'),
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
		'snurch': Key('c-l,c-e'),
		'BB search': Text('/'),
		'BB My work': Text('g,d'),
		'BB sidebar': Text('['),
		'BB filter': Text('f'),
		'BB comments': Text('tc'),
		'BB Overview': Text('pd'),
		'BB Activity': Text('pa'),
		'BB Commits': Text('pc'),

        # Common websites
        
        'Open zoom': Key("c-t") + Text(R"https://zoom.us/j/6516749931") + Key("enter"),
        'Open pipes': Key("c-t") + Text(R"https://dev.azure.com/inspirato-dev/PassList/_build") + Key("enter"),
        'Open tech docs': Key("c-t") + Text(R"https://docs.google.com/document/d/1XVYzcH_kkqa6Wr13Z654RdRuJ1j0mVRVMgU8_XSiTx0/edit") + Key("enter"),
        'Open Azure': Key("c-t") + Text("https://portal.azure.com/#home") + Key("enter"),
        'Open redis': Key("c-t") + Text("http://127.0.0.1:8081") + Key("enter"),
        'Open pluralsight': Key("c-t") + Text("https://app.pluralsight.com/library/") + Key("enter"),
        'open team city': Key("c-t") + Text("http://teamcity.inspirato.com") + Key("enter"),
        'Open pie docs': Key("c-t") + Text("https://pythonhosted.org/dragonfly/actions.html") + Key("enter"),
        'open team city <pascal_text>': Key("c-t") + Text("http://teamcity.inspirato.com/project.html?projectId=%(pascal_text)s") + Key("enter"),
        'open octo': Key("c-t") + Text("https://octo.inspirato.com:8000/app") + Key("enter"),
        'open bitbucket': Key("c-t") + Text("https://bitbucket.org/dashboard/overview") + Key("enter"),
        'Open Jira': Key("c-t") + Text("https://inspirato.atlassian.net/secure/RapidBoard.jspa?rapidView=315&assignee=557058%3A17c5d830-0332-4496-a9bd-a99169a75113") + Key("enter"),
        'Open wiki': Key("c-t") + Text("https://inspirato.atlassian.net/wiki/spaces/IN/overview?mode=global") + Key("enter"),
        'Open Gmail': Key("c-t") + Text("https://mail.google.com/mail/u/0/#inbox") + Key("enter"),
        'Open grammer chat': Key("c-t") + Text("https://gitter.im/dictation-toolbox/dragonfly?source=orgpage") + Key("enter"),
        'Open ticket <number>': Key("c-t") + Text("https://inspirato.atlassian.net/browse/DF-%(number)d") + Key("enter"),
        'Open trunk': Key("c-t") + Text("https://dryfly-trunk.dev.inspirato.com") + Key("enter"),
        'Open JS snippets': Key("c-t") + Text("https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets") + Key("enter"),

        # Web console
        'open debugger': Key('f12'),
        'goat': Key('c-p'),
        'run it': Key('f8'),
        'step over': Key('s-f11'),
        'step in': Key('f11'),
        'step out': Key('f10'),
        'elements tab': Key('c-1'),
        'Consol tab': Key('c-2'),
        'sources tab': Key('c-3'),
        'network tab': Key('c-4'),
        'performance tab': Key('c-5'),
        'line <number>': Key('c-g') + Text('%(number)d') + Key('enter'),
        'break snap': Key('c-f8'),
        'inspect': Key('cs-c'),
        
    }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 99999),
        Dictation("text"),
        Dictation("pascal_text", default="").title().replace(" ", ""),
    ]

context = AppContext(executable='chrome')
grammar=Grammar('Google Chrome',context=context)
grammar.add_rule(GlobalChromeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None