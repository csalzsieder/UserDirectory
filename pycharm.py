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
        'if main': Text("if __name__ == '__main__':"),

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
        'watch add': Key("c-w,w"),
        'watch rem': Key("c-w,r"),

        # open files
        'open scratch': Key("cas-insert")  + Text('py') + Key('enter'),

        # Editing
        'get usage': Key("a-f7"),
		'replace global': Key("cs-r"),
        'back space': Key('backspace'),
        'Div <text>': Text('<div>%(text)s</div>'),
        'Open folder': Key('c-k,c-o'),
        
        'copy down': Key('c-d'),
        'move up': Key('cs-up'),
        'move down': Key('cs-downgit com'),
		'Load web': Key('w-4') + Pause('50') + Key('f5') + Pause('50') + Key('w-5'),
        'copy line <number>': Key('c-g') + Text('%(number)d') + Key('enter,s-end,c-c'),
        'select line <number>': Key('c-g') + Text('%(number)d') + Key('enter,s-end'),
        'select multi <number>': Key("shift:down, ctrl:down, alt:down, down:%(number)d, shift:up, ctrl:up, alt:up,"),
        'line <number>': Key('c-g') + Pause('15') + Text('%(number)d') + Key('enter') + Pause('10') + Key('end'),
        'zap': Key("c-slash"),
        'nick': Key("a-left"),
        'tab <number>': Key('c-t,%(number)d'),
        # 'pin it': Key('c-It,%(number)d'),
        # 'Change language': Key('c-k,m'),c
        'New copy': Key('c-c,c-v'),
        'new pie': Key('a-insert') + Pause('20') + Key('p,f, enter'),
        'new module': Key('a-insert') + Pause('20') + Key('p, enter'),
        'new folder': Key('a-insert') + Pause('20') + Key('d, enter'),
        'open in files': Key('csa-o'),
        'load disk': Key('ca-y'),
        'split it': Key('csa-r'),
        'save it': Key('c-s'),
        

        # Re-factorring
        'loot': Key('a-enter'),
        'Ludi': Key('c-j'),
        'loot hint': Key('c-q'),
        'loot method': Key('ca-m'),
        'loot Sig': Key('c-f6'),
        'loot do': Key('a-d'),
        'loot move': Key('f6'),
        'loot surround': Key('ca-t'),
        'loot up': Key('cs-up'),
        'loot down': Key('cs-down'),
        'loot fun': Key('c-f12'),
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
        'view commit': Key('a-0'),
        'view see': Key('a-1'),
        'hide see': Key('s-escape'),
        'view favorite': Key('a-2'),
        'view find': Key('a-3'),
        'view run': Key('a-4'),
        'view bug': Key('a-5'),
        'view prob': Key('a-6'),
        'view con': Key('a-7'),
        'view git': Key('a-9'),
        'see match': Key('a-f1,1'),
        'see minus': Key('c-minus'),
        'see plus': Key('c-plus'),
        'set view': Key('ca-s'),
        'term view': Key("a-f12"),
        'book view': Key("s-f11"),
        'break view': Key("cs-f8"),
        'sigh view': Key('a-2'),
        'compare view': Key('c-d'),
        'sigh pan': Text('.limit(20).toPandas()'),
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
        'Goat all': Key('shift,shift'),
        'Goater': Key('c-e'),
        'Goat': Key('cs-g'),
        'Recent changes': Key('as-c'),
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
        'cd client': Text('cd src/libraries/client_src/') + Key('enter'),
        'cd common': Text('cd src/libraries/common_src/') + Key('enter'),
        'cd pass': Text(' cd src/projects/passlist_proj/passlist_src/') + Key('enter'),
        'cd inventory': Text(' cd src/projects/inventory_proj/inventory_src/') + Key('enter'), 
        'cd Rules': Text(' cd src/projects/rules_engine_proj/rules_engine_src/') + Key('enter'), 
        'cd payment': Text(' cd src/projects/payment_proj/payment_src/') + Key('enter'),
        'cd root': Text(' cd D:GitProjects/data-platform') + Key('enter'),



        # git 
        'get check out main': Function(gitPause) + Text("git co main && git pull && git fetch") + Key("enter"),
        'get check out feature': Function(gitPause) + Text("git co feature/"),
        'get fetch': Function(gitPause) + Text("git fetch") + Key('enter'),
        'get called <nospace>': Function(gitPause) + Text("git cob %(nospace)s/"),
        'get called ticket': Function(gitPause) +  Text("git cob feature/DP-"),
        'get checkout <text>': Function(gitPause) + Text("git co %(text)s/"),
        'get merge <text>': Function(gitPause) + Text("git merge --%(text)s"), #Continue, abort
        'get merge develop': Function(gitPause) + Text("git merge origin/develop") + Key('enter'),
        'get merge main': Function(gitPause) + Text("git merge origin/main") + Key('enter'),
        'get tags': Function(gitPause) + Text('git tag -l --sort=-v:refname') + Key('enter'),
        'get tag pass': Function(gitPause) + Text('git tag passlist/'),
        'get tag rules': Function(gitPause) + Text('git tag rules_engine/'),
        'get tag payment': Function(gitPause) + Text('git tag payment/'),
        'get tag <text>': Function(gitPause) + Text('git tag %(text)s/'),
        'get tag push': Text(' & git push origin --tag') + Key('enter'),
        'get commit': Function(gitPause) + Text('git commit -am ""') + Pause("10") + Key('left'),
        'get commit wip': Function(gitPause) + Text('git commit -am wip') + Key('enter'),
        'get push yes': Function(gitPause) + Text('git push') + Pause("10") + Key('enter'),
        'get push': Function(gitPause) + Text('git push') + Pause("10") + Key('enter'),
        'Get push menu': Key("c-g,p"),
        'get pull': Function(gitPause) + Text('git pull') + Pause("10") + Key('enter'),
        'get branch': Function(gitPause) + Text('git branch -r') + Pause("10") + Key('enter'),
        'get branches': Key('cs-`'),
        'get branch delete': Key('shift,shift') + Text('delete old branch') + Key('enter'),
        'get discard': Function(gitPause) + Text("git reset & git checkout -- .") + Pause("10") + Key('enter'),
        'get stash <text>': Function(gitPause) + Text("git stash %(text)s") + Key("enter"), #drop/pop
        'get stash': Function(gitPause) + Text("git stash") + Key("enter"), #drop/pop
        'get prune': Function(gitPause) + Text("git remote prune origin") + Key("enter"),
        'get PR': Key("cs-x,p"),
        'get recent': Key("as-c"),
        'get add': Key("ca-a"),

        # bazel
        'bay shut down': Function(gitPause) + Text("bazelisk shutdown") + Key("enter"),
        'bay version': Function(gitPause) + Text("bazelisk version") + Key("enter"),
        'bay build': Function(gitPause) + Text("bazelisk build "),
        'bay build pass': Function(gitPause) + Text("bazelisk build passlist") + Key('enter'),
        'bay build rules': Function(gitPause) + Text("bazelisk build rules_engine") + Key('enter'),
        'bay build payment': Function(gitPause) + Text("bazelisk build payment_venv") + Key('enter'),
        'bay build <text>': Function(gitPause) + Text("bazelisk build %(text)s"),

        # tests
        'test all': Function(gitPause) + Text("python -m unittest") + Key("enter"), #drop/pop

        #pip
        'pippy': Function(gitPause) + Text("pipenv "),
        'pip install': Function(gitPause) + Text("pipenv install"),
        'pip remove': Function(gitPause) + Text("pipenv --rm"),
        'pip develop': Function(gitPause) + Text("pipenv install --dev") + Key('enter'),
        'pip skip': Function(gitPause) + Text("pipenv install --dev --skip-lock") + Key('enter'),
        'pip run': Function(gitPause) + Text("pipenv run "),
        'pip instally': Function(gitPause) + Text("pipenv install '-e .'"),
        'pip install edit': Function(gitPause) + Text("pipenv install --editable "),
        'pip list': Function(gitPause) + Text("pipenv run pip list") + Key('enter'),
        'pip shell': Function(gitPause) + Text("pipenv shell") + Key('enter'),
        'pip clear': Function(gitPause) + Text("pipenv --clear") + Key('enter'),
        'pip lock clear': Function(gitPause) + Text("pipenv lock --clear") + Key('enter'),
        'pip sync': Function(gitPause) + Text("pipenv run pipenv-setup sync") + Key('enter'),
        'pip require': Function(gitPause) + Text("pipenv lock -r > requirements.txt") + Key('enter'),
        'pip exit': Function(gitPause) + Text("exit") + Key('enter'),


        # databricks cli
        'bricks <nocaps>': Function(gitPause) + Text("databricks %(nocaps)s"),
        'bricks secrets': Function(gitPause) + Text("databricks secrets list-scopes") + Key('enter'),
        'bricks scopes': Function(gitPause) + Text("databricks secrets list --scope"),
        'bricks connect': Function(gitPause) + Text("databricks-connect configure"),
        'bricks test': Function(gitPause) + Text("databricks-connect test"),
        'bricks push': Function(gitPause) + Text("databricks workspace import_dir . /passlist -o") + Key('enter'),

        # docker
        'dock list': Function(gitPause) + Text('docker ps -a') + Key('enter'),
        'dock rem': Function(gitPause) + Text('docker rm'),
        'dock start': Function(gitPause) + Text('docker start'),
        'dock stop': Function(gitPause) + Text('docker stop'),
        'dock logs': Function(gitPause) + Text('docker logs'),
        'dock compose': Function(gitPause) + Text('docker-compose up') + Key('enter'),
        'dock build ': Function(gitPause) + Text('docker-compose up --build') + Key('enter'),
        'dock to air': Function(gitPause) + Text('docker exec -it airflow_airflow-webserver_1 bash') + Key('enter'),
        # 'dock red': Function(gitPause) + Text('docker run --name redis -p 6379:6379 -d redis') + Key('enter'),
        # 'dock start red': Function(gitPause) + Text('docker start redis') + Key('enter'),

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