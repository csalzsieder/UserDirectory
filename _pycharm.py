#imports the library
from dragonfly import (Function,Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mimic)


def gitPause():
    Key('escape').execute()
    Pause('20').execute()
    Key('a-f12').execute()
    Pause("40").execute()

def repeat(number):
    s = 'cd '
    for i in range(0, number):
            s += '../'
    
    Text('{}'.format(s)).execute()

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
        'run it': Key("s-f10"),
        'bug it': Key("s-f9"),
        'play it': Key("f9"),
        'kill it': Key("c-f2"),
        # 'restart': Key("cs-f5"),
        'step in': Key('as-f7'),
        'step over': Key('f8'),
        'step out': Key("s-8"),
        'step to': Key("a-f9"),
        'break snap': Key("c-f8"),
        'break mute': Key("cas-f8"),

        # open files
        "Open pie": Key("c-k,c-o,a-d") + Pause('50') + Text(R'C:\NatLink\NatLink\MacroSystem') + Key("enter:2"),
        "Open react": Key("c-k,c-o,a-d") + Pause('50') + Text(R"D:\GitProjects\react-components") + Key("enter:2"),
        "Open code": Key("c-k,c-o,a-d") + Pause('50') + Text(R"D:\GitProjects") + Key("enter:2"),
        'open scratch': Key("cas-insert")  + Text('py') + Key('enter'),

        # Editing
        'get usage': Key("a-f7"),
        'replace local': Key("c-h"),
		'replace global': Key("cs-h"),
        'back space': Key('backspace'),
        'Div <text>': Text('<div>%(text)s</div>'),
        'Open folder': Key('c-k,c-o'),
        'New copy': Key('c-c,c-v'),
        'copy down': Key('c-d'),
		'Load web': Key('w-4') + Pause('50') + Key('f5') + Pause('50') + Key('w-5'),
        'copy line <number>': Key('c-g') + Text('%(number)d') + Key('enter,s-end,c-c'),
        'select line <number>': Key('c-g') + Text('%(number)d') + Key('enter,s-end'),
        'select multi <number>': Key("shift:down, ctrl:down, alt:down, down:%(number)d, shift:up, ctrl:up, alt:up,"),
        # 'line <number>': Key('c-g') + Pause('5') + Text('%(number)d'),
        'line <number>': Key('c-g') + Pause('15') + Text('%(number)d') + Key('enter') + Pause('10') + Key('end'),
        # 'line <number> <n>': Key('c-g') + Text('%(number)d') + Key('enter,end') + Key('left:%(n)d'),
        'zap': Key("c-k,c-c"),
        'meow': Key("c-k,c-u"),
        'nick': Key("a-left"),
        'del line': Key("s-delete"),
        'tab <number>': Key('c-t,%(number)d'),
        # 'pin it': Key('c-It,%(number)d'),
        'Change language': Key('c-k,m'),
        'py Phi': Key('a-insert,p,f, enter'),
        'py package': Key('a-insert,p, enter'),
        'py directory': Key('a-insert,d, enter'),
        # 'py con': Key('csa-p'),
        'bug con': Key('csa-r'),
        

        # Re-factorring
        'loot': Key('a-enter'),
        'loot hint': Key('c-q'),
        'loot method': Key('ca-m'),
        'loot Sig': Key('c-f6'),
        'loot do': Key('a-d'),
        'loot move': Key('f6'),
        'loot surround': Key('ca-t'),
        'loot up': Key('cs-up'),
        'loot down': Key('cs-down'),
        'to do': Text('# TODO:'),

        # Navigation
        'snurch': Key('cs-f'),
        'snurch win': Key('csa-y'),
        'previ': Key('a-left'),
        'nexty': Key('a-right'), 
        # 'Save all': Key('c-k,s'),
        # 'Save': Key('c-s'),
        'clean code': Key('ca-l'),
        'clean file': Key('cas-l'),
        'Edit config': Key('csa-e '),
        'select run': Key('c-s, c-r'),

        # views
        'commit view': Key('a-0'),
        'see view': Key('a-1'),
        'favorite view': Key('a-2'),
        'find view': Key('a-3'),
        'run view': Key('a-4'),
        'bug view': Key('a-5'),
        'prob view': Key('a-6'),
        'con view': Key('a-7'),
        'git view': Key('a-9'),
        'see match': Key('a-f1,1'),
        'set view': Key('ca-s'),
        'term view': Key("a-f12"),
        'book view': Key("s-f11"),
        'break view': Key("cs-f8"),
        
        'sigh view': Key('a-2'),
        'sigh pan': Text('.limit(20).toPandas()') + Key('enter'),
        'to pan': Text('.toPandas()') + Key('enter'),
        'show me': Text('.show()') + Key('enter'),
        'count me': Text('.count()') + Key('enter'),


        # Navigation
        # 'Open tab': Key('c-n'),
        'book snap': Key('f11'),
        'book snap <number>': Key('c-f11') + Pause('50') + Key('%(number)d'),
        'book <number>': Key('c-%(number)d'),
        'find death': Key('sa-f12'),
        'goat in': Key('ca-b'),
        'Goat': Key('cs-n'),
        'Goater': Key('c-e'),
        'Goat funk': Key('cs-o'),
        'Goat prop': Key('cs-p'),
        'close all': Key('cs-f4'),
        'close tab': Key('c-f4'),
        'close others': Key('cas-f4'),
        'close pin': Key('cas-p'),
        'close right': Key('cas-r'),
        'pin it': Key('cas-q'),
        'key cuts': Key('c-k, c-s'),
        'rename': Key('s-f6'),
        'doneUnder': Text('__'),
        'quote': Text("'"),
        'Eck': Text(" = "),
        'py con': Key('cs-u'),
        'replace': Key('c-r'),
        # '<nocaps>': Text('%(noccaps)s'),
        # Commands
        'Execute <text>': Key('cs-p') + Text('Execute %(text)s') + Key('enter'), #Query, selected

        # terminal navigation
        'cd <lowtext>':  Function(gitPause) + Text('cd %(lowtext)s') + Key('enter'),
        'cd back':  Function(gitPause) + Text('cd ..') + Key('enter'),
        'cd <number>': Function(repeat) + Key('enter'),

        # git 
        'get check out master': Function(gitPause) + Text("git co master && git pull && git fetch") + Key("enter"),
        'get check out main': Function(gitPause) + Text("git co main && git pull && git fetch") + Key("enter"),
        'get check out feature': Function(gitPause) + Text("git co feature/"),
        'get fetch': Function(gitPause) + Text("git fetch") + Key('enter'),
        'get called <nospace>': Function(gitPause) + Text("git cob %(nospace)s/"),
        'get called ticket': Function(gitPause) +  Text("git cob feature/DF-"),
        'get checkout <text>': Function(gitPause) + Text("git co %(text)s/"),
        'get merge <text>': Function(gitPause) + Text("git merge --%(text)s"), #Continue, abort
        'get merge develop': Function(gitPause) + Text("git merge origin/develop") + Key('enter'),
        'get merge master': Function(gitPause) + Text("git merge origin/master") + Key('enter'),
        'get tags': Function(gitPause) + Text('git tag -l --sort=-v:refname') + Key('enter'),
        'get tag': Function(gitPause) + Text('git tag version/'),
        'get tag push': Text(' & git push origin --tag') + Key('enter'),
        'get commit': Function(gitPause) + Text('git commit -am ""') + Pause("10") + Key('left'),
        'get commit wip': Function(gitPause) + Text('git commit -am wip') + Key('enter'),
        'get push yes': Function(gitPause) + Text('git push') + Pause("10") + Key('enter'),
        'get push': Function(gitPause) + Text('git push --no-verify') + Pause("10") + Key('enter'),
        'Get push menu': Key("c-g,p"),
        'get pull': Function(gitPause) + Text('git pull') + Pause("10") + Key('enter'),
        'get branch': Function(gitPause) + Text('git branch -r') + Pause("10") + Key('enter'),
        'get branches': Key('cs-`'),
        'get discard': Function(gitPause) + Text("git checkout -- .") + Pause("10") + Key('enter'),
        'get stash <text>': Function(gitPause) + Text("git stash %(text)s") + Key("enter"), #drop/pop
        'get stash': Function(gitPause) + Text("git stash") + Key("enter"), #drop/pop
        'get prune': Function(gitPause) + Text("git remote prune origin") + Key("enter"),
        'get PR': Key("cs-x,p"),
        'get recent': Key("as-c"),
        'get add': Key("ca-a"),

        # bazel
        'bay shut down': Function(gitPause) + Text("bazel shutdown") + Key("enter"),
        'bay version': Function(gitPause) + Text("bazel version") + Key("enter"),
        'bay build': Function(gitPause) + Text("bazel build "),

        # tests
        'test all': Function(gitPause) + Text("python -m unittest") + Key("enter"), #drop/pop

        #pip
        'pip install': Function(gitPause) + Text("pipenv install") + Key('enter'),
        'pip develop': Function(gitPause) + Text("pipenv install --dev") + Key('enter'),
        'pip run': Function(gitPause) + Text("pipenv run "),
        'pip instally': Function(gitPause) + Text("pipenv install '-e .'"),
        'pip install edit': Function(gitPause) + Text("pipenv install --editable "),
        'pip list': Function(gitPause) + Text("pipenv run pip list") + Key('enter'),
        'pip shell': Function(gitPause) + Text("pipenv shell") + Key('enter'),
        'pip sync': Function(gitPause) + Text("pipenv run pipenv-setup sync") + Key('enter'),
        'pip exit': Function(gitPause) + Text("exit") + Key('enter'),


        # databricks cli
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
        Integer('numberdot', 1, 9999),
        Integer('n', 1, 9999),
        Dictation("text"),
        Dictation("nocaps", default="").lower(),
        Dictation("camel_text", default="").camel(),
        Dictation("snaketext", default="").lower().replace(" ", "_"),
        Dictation("nospace", default="").lower().replace(" ", ""),
        Dictation("lowtext", default="").lower(), 
    ]

context = AppContext(executable='pycharm64')
grammar=Grammar('Pycharm',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None