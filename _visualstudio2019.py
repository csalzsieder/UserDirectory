#imports the library
from dragonfly import (Function, Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause)

def book_number(number):
    Key("c-k,c-w").execute()
    Pause('30').execute()
    Key("home").execute() 
    stroke = "{}{}".format('down:',number-1)
    Key(stroke).execute()
    Key('enter').execute()

class VisualStudioMappings(MappingRule):
    mapping = {  
        # temp
        'Add navigation': Text('~/Views/Navigation/Header/Navigation'),
        'Add header': Text('~/Views/Navigation/Header'),
        'Add Extension': Text('.cshtml'),

        # Bookmarks
        'book <number>': Function(book_number),  
        'book snap': Key("c-k,c-k"),
        'book nexty': Key("c-k,c-n"),
        'book previ': Key("c-k,c-p"),
        'book view': Key("c-k,c-w"),
        'book clear': Key("c-k,c-l, enter"),
        
        # Navigation
        'snurch': Key("cs-f"),
        'Goat amp': Key('c-f12'),
        'goat death': Key('f12'),
        'peak death': Key('a-f12'),
        'view recent': Key('c-t,r'),
        'view edits': Key('cs-comma'),
        'All ref': Key('c-f12'),
        'Format doc': Key('c-k,c-d'),
        'line <number>': Key("c-g") + Text("%(number)s") + Key("enter,end"),
        'close tab': Key("c-f4"),
        'close all': Key("a-minus")+ Pause('50') + Key('a'),
        'close pinned': Key("a-minus")+ Pause('50') + Key('down:6, enter'),
        'pin tab': Key("a-minus")+ Pause('50') + Key('p'),
        'save all': Key("cs-s"),
        'delete line': Key("s-delete"),
        'Sink dock': Key("c-[,s"),
        'goat': Key("c-t"),
        'goat to': Key("c-comma"),
        'X open': Key("ca-l"),
        'terminal open': Key("c-backslash,c-backslash"),
        'tab select': Key('ctrl:down,tab'),
        'next wrath': Key('cs-down'),
        'pick <number>': Key('down:%(number)s, enter, ctrl:up'),

        # Debugging
        'step in': Key('f5'),
        'step over': Key('f10'),
        'step out': Key("s-f11"),
        'Break snap': Key("f9"),
        'Break view': Key("ca-b"),
        'Run it': Key("f5"),
        'Attach <number>': Key("c-r,c-%(number)s"),
        'watch <number>': Key('ca-w,%(number)s'),
        'tests run': Key('c-r,t'),
        'test debug': Key('c-r') + Pause('20') + Key('c-t'),
        'Blossom': Key("cs-b"),
        'blessed load': Key("cs-b") + Pause('800') + Key('w-4') + Pause('50') + Key('c-1,f5') + Pause('50') + Key('w-6'),
        'Load web': Key('w-4') + Pause('50') + Key('c-1,f5') + Pause('50') + Key('w-6'),
        'kill it': Key('s-f5'),
        'fill sir': Key('c-;'),

        # editing
        'Blossom': Key("cs-b"),
        'blessed load': Key("cs-b") + Pause('800') + Key('w-4') + Pause('50') + Key('c-1,f5') + Pause('50') + Key('w-6'),
        'Load web': Key('w-4') + Pause('50') + Key('c-1,f5') + Pause('50') + Key('w-6'),
        'surround with': Key('c-e, c-u'),
        'line comment': Key('c-k,c-c'),
        'line uncomment': Key('c-k,c-u'),
        'Replace all' : Key('a-a'),
        'goat replace' : Key('c-h'),
        'Clean code' : Key('c-k,c-e'),
        'Surround with' : Key('c-k,c-s'),
        'Show info' : Key('c-k,c-i'),
        'zoom in' : Key('cs-<'),
        'zoom out' : Key('cs->'),
        'add class': Key('ca-insert, down:6, enter'),
        'add controller': Key('ca-insert,enter'),
        'add Item': Key('cs-a'),
        'move up': Key('a-up'),
        'move down': Key('a-down'),
        'Loot': Key('c-.'),
        'rename': Key('c-r,c-r'),
        
        # git 
        'get called <number> <dashtext>':Key("ca-l") + Key("c-backslash,c-backslash") + Text("git cob feature/DF-%(number)s-%(dashtext)s"),
        'get check out develop':Key("ca-l") + Key("c-backslash,c-backslash") + Text("git co develop") + Key("enter"),
        'get check out <nospace>':Key("ca-l") + Key("c-backslash,c-backslash") + Text("git co %(nospace)s/"),
        'get check out MC':Key("ca-l") + Key("c-backslash,c-backslash") + Text("git co feature/new-mcapi-integration") + Key('enter'),
        'get discard':Key("ca-l") + Key("c-backslash,c-backslash") + Text("git checkout -- .") + Key("enter"),
        'get merge <text>':Key("ca-l") + Key("c-backslash,c-backslash") + Text("git merge --%(text)s") + Key("enter"), #Abort, merge
        'get merge develop':Key("ca-l") + Key("c-backslash,c-backslash") + Text("git merge origin/develop") + Key("enter"),
        'get merge feature':Key("ca-l") + Key("c-backslash,c-backslash") + Text("git merge feature/DF-"),
        'get pull':Key("ca-l") + Key("c-backslash,c-backslash") + Text("git pull") + Key("enter"),
        'get push':Key("ca-l") + Key("c-backslash,c-backslash") + Text("git push") + Key("enter"),
        'get stash': Key("c-backslash,c-backslash") + Text("git stash") + Key("enter"),
        'get stash <text>':Key("ca-l") + Key("c-backslash,c-backslash") + Text("git stash %(text)s") + Key("enter"), #drop/pop
        'get commit <text>':Key("ca-l") + Key("c-backslash,c-backslash") + Text('git add -A && git commit -m "%(text)s"'),
        # 'get add': Key("c-backslash,c-backslash") + Text('git add -A') + Key('enter'),
        

        # Snippets
        'Open snippets': Key('c-k,c-b'),
        'prop snip': Text('prop') + Key('tab:2'),
        'See tour snip': Text('ctor') + Key('tab'),

        # Opening solutions
        'Open solution': Key("cs-o"),

    }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 0, 9999),
        Dictation("text"),
        Dictation("dashtext", default="").lower().replace(" ", "-"),
        Dictation("nospace", default="").lower().replace(" ", ""),
    ]

context = AppContext(executable='devenv')
grammar=Grammar('Visual Studio',context=context)
grammar.add_rule(VisualStudioMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None