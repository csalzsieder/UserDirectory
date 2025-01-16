#imports the library
import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
from xml.dom import pulldom
from dragonfly import (Function,Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mimic)

def gitPause():
    Key('alt').execute() 
    Pause('10').execute()
    Key('c-`').execute() 
    Pause("10").execute()

def repeat(number):
    s = 'cd '
    for i in range(0, number):
            s += '../'
    
    Text('{}'.format(s)).execute()
    
class CodeMappings(MappingRule):
    mapping = {  
        # Snippets
        # 'text snip': Text("Text('')") + Pause('30') + Key('left:2'),
        # 'key snip': Text("Key('')") + Pause('30') + Key('left:2'),
        # 'pause snip': Text("Pause('')") + Pause('30') + Key('left:2'),
        # 'pie def': Text('df'),
        # 'in com': Text('# COMMAND ----------'),


        # Python
        'py com': Text('##############################') + Key('enter') + Text('# '),
        'py com end': Text('##############################') + Key('enter'),

        # debugging
        'play it': Key("f5"),
        'bug it': Key("c-1") + Key("f5") + Pause('10'),
        'kill it': Key("s-f5"),
        'restart': Key("cs-f5"),
        'step in': Key('f11'),
        'step over': Key('f10'),
        'step out': Key("s-f11"),
        'breaks snap': Key("f9"),
        'watch add': Key("c-a,c-w"),

        # open files
        "Open pie": Key("c-k,c-o,a-d") + Pause('50') + Text(R'C:\NatLink\NatLink\MacroSystem') + Key("enter:2"),
        "Open react": Key("c-k,c-o,a-d") + Pause('50') + Text(R"D:\GitProjects\react-components") + Key("enter:2"),
        "Open code": Key("c-k,c-o,a-d") + Pause('50') + Text(R"D:\GitProjects") + Key("enter:2"),

        # Editing
        'back space': Key('backspace'),
        'New copy': Key('c-c,c-v'),
        'copy down': Key('as-down'),
		'Load web': Key('w-4') + Pause('50') + Key('f5') + Pause('50') + Key('w-5'),
        'copy line <number>': Key('c-g') + Text('%(number)d') + Key('enter,s-end,c-c'),
        'select line <number>': Key('c-g') + Text('%(number)d') + Key('enter,s-end'),
        'select multi <number>': Key("shift:down, ctrl:down, alt:down, down:%(number)d, shift:up, ctrl:up, alt:up,"),
        # 'line <number>': Key('c-g') + Pause('5') + Text('%(number)d'),
        'line <number>': Key('c-g, c-l') + Text('%(number)d') + Key('enter,end'),
        # 'line <number> <n>': Key('c-g') + Text('%(number)d') + Key('enter,end') + Key('left:%(n)d'),
        'zap': Key("c-k,c-c"),
        'zip': Key("c-k,c-u"),
        'tab <tab>': Key('a-%(tab)d'),
        'Change language': Key('c-k,m'),
        'split it': Key('c-backslash'),
        'new file': Key('ca-n'),
        'replace': Key('c-h'),

        # codeso/yeah



        # Re-factorring
        'loot': Key('c-.'),
        # 'Ludi': Key('c-j'),
        'loot hint': Key('c-q'),
        'loot ref': Key('s-f12'),
        'loot trim': Key('c-k,c-xs'),
        'loot method': Key('cs-r'),
        'loot find': Key('cs-o'),
        'loot co': Key('c-i'),
        # 'loot do': Key('a-d'),
        # 'loot move': Key('f6'),
        # 'loot surround': Key('ca-t'),
        # 'loot up': Key('cs-up'),
        # 'loot down': Key('cs-down'),
        # 'loot fun': Key('c-f12'),
        # 'to do': Text('# TODO:'),

        # Navigation
        'snurch': Key('cs-f'),
        'pallet': Key('cs-p'),
        'nexty': Key('c-pgdown'), 
        'Save all': Key('c-k,s'),
        'Save': Key('c-s'),
        'view see': Key('cs-e'),
        'view bar': Key('ca-b'),
        'view bug': Key('cs-y'),
        'view toggle': Key('c-b'),
        'view source': Key('cs-g,g'),
        'view shell':Key('c-`'),
        'view set':Key('c-comma'),
        'view extension':Key('cs-x'),
        'view test':Key('c-v,c-t'),
        'view keys':Key('c-k,c-s'),
        'goat branches':Key('c-g,c-o'),
        'view interpreter':Key('c-p,c-i'),
        'see minus': Key('c-c,c-'),
        'new shell':Key('cs-`'),
        'shelly':Key('c-pageup'),
        'Open tab': Key('c-n'),
        'Open folder': Key('c-k,c-o'),
        'Sidebar': Key('c-b'),
        'goat reference': Key('sa-f12'),
        'goat in': Key('f12'),
        'goat usage': Key('s-f12'),
        'goat peak': Key('a-f12'),
        'goat side': Key('c-k,f12'),
        'Goat': Key('c-e'),
        'Goat funk': Key('cs-o'),
        'Goat prop': Key('cs-p'),
        'focus code': Key('c-j'),
        'close all': Key('c-k,w'),
        'close tab': Key('c-f4'),
        'close others': Key('c-c,o'),
        'paste offerings': Text('src\projects\merchandising_proj\pass_offerings_src'),
        
        'rename': Key('f2'),
        'doneUnder': Text('__'),

        # gpt
        'chat spark': Key('ca-i') + Pause('30') + Text('pyspark '),
        'chat py': Key('ca-i') + Pause('30') + Text('python '),
        'chat': Key('ca-i'),
        
        # bookmarks
        'book snap': Key('c-b,c-k'),
        'book list': Key('c-b,c-l'),
        'book snap <number>': Key('cs-%(number)d') + Pause('50') + Key(''),
        'book <number>': Key('c-%(number)d'),
        'see minus': Key('c-b,c-c'),
               
        # search and replace
        'replace local': Key("c-h"),
		'replace global': Key("cs-h"),

        # terminal navigation
        # 'cd <lowtext>':  Text('cd %(lowtext)s') + Key('enter'),
        'cd back': Text('cd ..') + Key('enter'),
        'cd <number>': Function(repeat) + Key('enter'),
        'cd client': Text('cd src/libraries/client_src/') + Key('enter'),
        'cd common': Text('cd src/libraries/common_src/') + Key('enter'),
        'cd pass': Text(' cd src/projects/passlist_proj/passlist_src/') + Key('enter'),
        'cd inventory': Text(' cd src/projects/inventory_proj/inventory_src/') + Key('enter'), 
        'cd Rules': Text(' cd src/projects/rules_engine_proj/rules_engine_src/') + Key('enter'), 
        'cd payment': Text(' cd src/projects/payment_proj/payment_src/') + Key('enter'),
        'cd root': Text(' cd D:GitProjects/data-platform') + Key('enter'),

        # git 
        'get merge main': Function(gitPause) + Text("git merge origin/main") + Key('enter'),
        'get check out main': Function(gitPause) + Text("git checkout main && git pull && git fetch") + Key("enter"),
        'get check out feature': Function(gitPause) + Text("git co feature/"),
        'get fetch': Function(gitPause) + Text("git fetch") + Key('enter'),
        # 'get called <nospace>': Function(gitPause) + Text("git cob %(nospace)s/"),
        'get called ticket': Function(gitPause) +  Text("git checkout -b feature/DP-"),
        'get called feature': Function(gitPause) +  Text("git checkout -b feature/"),
        'get checkout <text>': Function(gitPause) + Text("git co %(text)s/"),
        'get merge <text>': Function(gitPause) + Text("git merge --%(text)s"), #Continue, abort
        
        'get tags': Function(gitPause) + Text('git tag -l --sort=-v:refname') + Key('enter'),
        'get tag push': Text(' & git push origin --tag') + Key('enter'),
        'get tag pass': Function(gitPause) + Text('git tag pass_offerings/'),
        'get tag rules': Function(gitPause) + Text('git tag pass_rules_engine/'),
        'get tag payment': Function(gitPause) + Text('git tag payment/'),
        'get tag invited': Function(gitPause) + Text('git tag invited_ultra_premium/'),
        'get tag <text>': Function(gitPause) + Text('git tag %(text)s/'),
        'get patch manager': Function(gitPause) + Text('push_tags -p uc_manager') + Key('enter'),
        'get patch pass': Function(gitPause) + Text('push_tags -p pass_offerings') + Key('enter'),
        'get patch <snaketext>': Function(gitPause) + Text('push_tags -p %(snaketext)s') + Key('enter'),
        'get minor <snaketext>': Function(gitPause) + Text('push_tags -m %(snaketext)s') + Key('enter'),
        'get tag delete': Text('git tag -d '),
        'get tag pull': Text('git pull --tags -f') + Key('enter'),
        'get commit': Function(gitPause) + Text('git commit -am ""') + Pause("10") + Key('left'),
        'get commit wip': Function(gitPause) + Text('git commit -am wip') + Key('enter'),
        'get commit trigger': Function(gitPause) + Text('git commit -am trigger-dbx-jobs') + Key('enter'),
        'get push yes': Function(gitPause) + Text('git push') + Pause("10") + Key('enter'),
        'get push': Function(gitPause) + Text('git push') + Pause("10") + Key('enter'),
        'get sink': Function(gitPause) + Text('git commit -am wip & git push') + Key('enter'),
        'Get push menu': Key("c-g,p"),
        'get pull': Function(gitPause) + Text('git pull') + Pause("10") + Key('enter'),
        'get branch': Function(gitPause) + Text('git branch -r') + Pause("10") + Key('enter'),
        'get branches': Key('cs-`'),
        'get branch delete': Key('shift,shift') + Text('delete old branch') + Key('enter'),
        'get discard': Function(gitPause) + Text("git reset & git checkout -- .") + Pause("10") + Key('enter'),
        'get stash <text>': Function(gitPause) + Text("git stash %(text)s") + Key("enter"), #drop/pop
        'get stash': Function(gitPause) + Text("git stash") + Key("enter"), #drop/pop
        'get prune': Function(gitPause) + Text("git remote prune origin") + Key("enter"),
        'get upstream': Function(gitPause) + Text("git branch --set-upstream-to=origin/"),
        'get project': Function(gitPause) + Text("cd D:/GitProjects/data-platform/src") + Key("enter"),
        'get PR': Key("cs-x,p"),
        'get recent': Key("as-c"),
        'get add': Key("ca-a"),

        # toggle
        'toggle <text>': Function(gitPause) + Text("python toggle_environment.py %(text)s") + Key("enter"),

        # bazel
        'bay shut down': Function(gitPause) + Text("bazelisk shutdown") + Key("enter"),
        'bay version': Function(gitPause) + Text("bazelisk version") + Key("enter"),
        'bay build': Function(gitPause) + Text("bazelisk build "),
        'bay build pass': Function(gitPause) + Text("bazelisk build pass_offerings_venv") + Key('enter'),
        'bay build rules': Function(gitPause) + Text("bazelisk build pass_rules_engine_venv") + Key('enter'),
        'bay build payment': Function(gitPause) + Text("bazelisk build payment_venv") + Key('enter'),
        'bay build <text>': Function(gitPause) + Text("bazelisk build %(text)s"),

        # tests
        'test all': Function(gitPause) + Text("python -m pytest") + Key("enter"), #drop/pop

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
        'pip lock': Function(gitPause) + Text("pipenv lock -r > requirements.txt") + Key('enter'),
        'pip sync': Function(gitPause) + Text("pipenv run pipenv-setup sync") + Key('enter'),
        'pip require': Function(gitPause) + Text("pip install -r requirements.txt") + Key('enter'),
        'pip exit': Function(gitPause) + Text("exit") + Key('enter'),
        'pip interpreter': Key('cs-p') + Text("python in") + Key("enter"),
        'pip graph': Key('cs-p') + Text("pipenv graph") + Key("enter"),


        # databricks cli
        # 'bricks <nocaps>': Function(gitPause) + Text("databricks %(nocaps)s"),
        'bricks connect': Function(gitPause) + Text("databricks-connect configure"),
        'bricks test': Function(gitPause) + Text("databricks-connect test"),

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


        'move file': Key('f2,c-c,a-t,c-v,a-t,down'),

    }
    extras=[
        Integer('tab', 1, 20),
        Integer('number', 1, 9999),
        Integer('n', 1, 9999),
        Dictation("text"),
        Dictation("nocaps", default="").lower(),
        Dictation("camel_text", default="").camel(),
        Dictation("snaketext").lower().replace(" ", "_"),
    ]

context = AppContext(executable='code')
grammar=Grammar('Visual Studio Code',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None