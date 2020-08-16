#imports the library
from dragonfly import (Function,Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mimic)


def gitPause():
    Key('escape').execute()
    Pause('10').execute()
    Key('csa-t').execute()
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
        'play it': Key("csa-f5"),
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
        'line <number>': Key('c-g') + Pause('10') + Text('%(number)d') + Key('enter') + Pause('10') + Key('end'),
        # 'line <number> <n>': Key('c-g') + Text('%(number)d') + Key('enter,end') + Key('left:%(n)d'),
        'oink': Key("c-k,c-c"),
        'meow': Key("c-k,c-u"),
        'del line': Key("s-delete"),
        'tab <tab>': Key('a-%(tab)d'),
        'Change language': Key('c-k,m'),
        'py file': Key('csa-n'),
        'py package': Key('csa-p'),
        'py con': Key('csa-p'),
        'bug con': Key('csa-r'),
        'loot': Key('c-.'),

        # Navigation
        'snurch': Key('cs-f'),
        'snurch win': Key('csa-y'),
        'previ': Key('c-pgup'),
        'nexty': Key('c-pgdown'), 
        'Save all': Key('c-k,s'),
        'Save': Key('c-s'),
        'clean code': Key('as-f'),

        # views
        'see view': Key('csa-e'),
        'book view': Key('csa-b'),
        'settings view': Key('c-comma'),
        'git view': Key('cs-g'),
        'commit view': Key('csa-q'),
        'term view': Key('csa-t'),
        'sigh view': Key('csa-s'),
        'sigh view': Key('csa-y'),
        'sigh pan': Text('.limit(50).toPandas()') + Key('enter'),

        'Open tab': Key('c-n'),
        'book snap': Key('c-f11'),
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
        'get check out master': Function(gitPause) + Text("git co master && git pull") + Key("enter"),
        'get check out feature': Function(gitPause) + Text("git co feature/"),
        'get called release': Function(gitPause) + Text("git cob release/"),
        'get called feature': Function(gitPause) +  Text("git cob feature/DF-"),
        'get checkout <text>': Function(gitPause) + Text("git co %(text)s/"),
        'get merge <text>': Function(gitPause) + Text("git merge --%(text)s"), #Continue, abort
        'get merge develop': Function(gitPause) + Text("git merge origin/develop") + Key('enter'),
        'get merge master': Function(gitPause) + Text("git merge origin/master") + Key('enter'),
        'get commit': Function(gitPause) + Text('git commit -am ""') + Pause("10") +         Key('left'),
        'get push': Function(gitPause) + Text('git push') + Pause("10") + Key('enter'),
        'get pull': Function(gitPause) + Text('git pull') + Pause("10") + Key('enter'),
        'get branch': Function(gitPause) + Text('git branch -r') + Pause("10") + Key('enter'),
        'get discard': Function(gitPause) + Text("git checkout -- .") + Pause("10") + Key('enter'),

        #pip
        'pip requirements': Function(gitPause) + Text("pip install -r requirements.txt") + Pause("10") + Key('enter'),


        # databricks clie
        'bricks <nocaps>': Function(gitPause) + Text("databricks %(nocaps)s"),
        'bricks secrets': Function(gitPause) + Text("databricks secrets list-scopes") + Key('enter'),
        'bricks scopes': Function(gitPause) + Text("databricks secrets list --scope"),

        # Builds
        'yarn <text>': Key('csa-t') + Pause('10') + Text("yarn %(text)s") + Key("enter"), #install, lint, clean, build, dev
        'load wheel': Function(gitPause) + Text('loadWheelToCluster.sh') + Key('enter'),
        'build wheel': Function(gitPause) + Text('loadWheelToCluster.sh') + Key('enter'),

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

context = AppContext(executable='pycharm64')
grammar=Grammar('Pycharm',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None