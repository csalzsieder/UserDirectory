#imports the library
from dragonfly import (Function,Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mimic)


def gitPause():
    Key('escape').execute()
    Pause('10').execute()
    Key('a-4').execute()
    Pause("10").execute()

class CodeMappings(MappingRule):
    mapping = {  
        # Snippets
        'crag test snip': Text('text'),
        'key snip': Text('key') + Pause('50') + Key('tab'),
        'pause snip': Text('pau') + Pause('50') + Key('tab'),
        'pie def': Text('def'),
        'in com': Text('# COMMAND ----------'),

        # Python
        'py commment': Text('##############################') + Key('enter') + Text('# '),
        'py commment end': Text('##############################') + Key('enter'),

        # debugging
        'run it': Key("c-f5"),
        'bugger': Key("f5"),
        'play it': Key("f7"),
        'kill it': Key("s-f5"),
        # 'restart': Key("cs-f5"),
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
        'line <number>': Key('c-g') + Pause('15') + Text('%(number)d') + Key('enter') + Pause('10') + Key('end'),
        # 'line <number> <n>': Key('c-g') + Text('%(number)d') + Key('enter,end') + Key('left:%(n)d'),
        'zap': Key("c-k,c-c"),
        'meow': Key("c-k,c-u"),
        'del line': Key("s-delete"),
        'tab <number>': Key('ca-%(number)d'),
        'Change language': Key('c-k,m'),
        'py Phi': Key('a-insert'),
        'py package': Key('csa-p'),
        # 'py con': Key('csa-p'),
        'bug con': Key('csa-r'),
        'loot': Key('c-.'),

        # Navigation
        'snurch': Key('cs-f'),
        'snurch win': Key('csa-y'),
        'previ': Key('c-pgup'),
        'nexty': Key('c-pgdown'), 
        'Save all': Key('c-k,s'),
        'Save': Key('c-s'),
        'clean up': Key('as-f'),

        # views
        'see view': Key('a-3'),
        'book view': Key('c-s,b'),
        'settings view': Key('c-comma'),
        'git view': Key('cs-g'),
        'commit view': Key('a-0'),
        'bug view': Key('cs-d'),
        'bug con': Key('csa-p'),
        'term view': Key("a-4"),
        'py con': Key('a-1'),
        'sigh view': Key('a-2'),
        'sigh pan': Text('.limit(20).toPandas()') + Key('enter'),
        'show me': Text('.show()') + Key('enter'),
        'count me': Text('.count()') + Key('enter'),


        'Open tab': Key('c-n'),
        'book snap': Key('c-f11'),
        'book snap <number>': Key('c-f11') + Pause('10') + Key('%(number)d'),
        'book <number>': Key('c-%(number)d'),
        'find death': Key('sa-f12'),
        'goat in': Key('f12'),
        'Goat': Key('c-p'),
        'Goater': Key('c-r'),
        'Goat funk': Key('cs-o'),
        'Goat prop': Key('cs-p'),
        'close all': Key('c-k, c-w'),
        'close tab': Key('c-w'),
        'close others': Key('c-k,c-o'),
        'key cuts': Key('c-k, c-s'),
        'rename': Key('f2'),
        'doneUnder': Text('__'),
        'py con': Key('cs-u'),
        'replace': Key('c-h'),
        # '<nocaps>': Text('%(noccaps)s'),
        # Commands
        'Execute <text>': Key('cs-p') + Text('Execute %(text)s') + Key('enter'), #Query, selected

        # git 
        'get check out develop': Function(gitPause) + Text("git co develop && git pull") + Key("enter"),
        'get check out feature': Function(gitPause) + Text("git co feature/"),
        'get called <nospace>': Function(gitPause) + Text("git cob %(nospace)s/"),
        'get called ticket': Function(gitPause) +  Text("git cob feature/DF-"),
        'get checkout <text>': Function(gitPause) + Text("git co %(text)s/"),
        'get merge <text>': Function(gitPause) + Text("git merge --%(text)s"), #Continue, abort
        'get merge develop': Function(gitPause) + Text("git merge origin/develop") + Key('enter'),
        'get merge master': Function(gitPause) + Text("git merge origin/master") + Key('enter'),
        'get commit': Function(gitPause) + Text('git commit -am ""') + Pause("10") + Key('left'),
        'get commit wip': Function(gitPause) + Text('git commit -am wip') + Key('enter'),
        'get push': Function(gitPause) + Text('git push') + Pause("10") + Key('enter'),
        'get pull': Function(gitPause) + Text('git pull') + Pause("10") + Key('enter'),
        'get branch': Function(gitPause) + Text('git branch -r') + Pause("10") + Key('enter'),
        'get discard': Function(gitPause) + Text("git checkout -- .") + Pause("10") + Key('enter'),
        'get stash <text>': Function(gitPause) + Text("git stash %(text)s") + Key("enter"), #drop/pop
        'get stash': Function(gitPause) + Text("git stash") + Key("enter"), #drop/pop

        #pip
        'pip requirements': Function(gitPause) + Text("pip install -r requirements.txt") + Pause("10") + Key('enter'),


        # databricks clie
        'bricks <nocaps>': Function(gitPause) + Text("databricks %(nocaps)s"),
        'bricks secrets': Function(gitPause) + Text("databricks secrets list-scopes") + Key('enter'),
        'bricks scopes': Function(gitPause) + Text("databricks secrets list --scope"),
        'bricks connect': Function(gitPause) + Text("databricks-connect configure"),
        'bricks push': Function(gitPause) + Text("databricks workspace import_dir . /passlist -o") + Key('enter'),

        # Builds
        'yarn <text>': Key('csa-t') + Pause('10') + Text("yarn %(text)s") + Key("enter"), #install, lint, clean, build, dev
        'load wheel': Function(gitPause) + Text('loadWheel.sh') + Key('enter'),
        'build wheel': Function(gitPause) + Text('buildWheel.sh') + Key('enter'),

        # 'test': bar("text"),  
    }
    extras=[
        Integer('number', 1, 9999),
        Integer('n', 1, 9999),
        Dictation("text"),
        Dictation("nocaps", default="").lower(),
        Dictation("camel_text", default="").camel(),
        Dictation("snaketext", default="").lower().replace(" ", "_"),
        Dictation("nospace", default="").lower().replace(" ", ""),
    ]

context = AppContext(executable='pycharm64')
grammar=Grammar('Pycharm',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None