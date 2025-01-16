from dragonfly import (StartApp, Function, Mimic, Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mouse)

def repeat(number):
    for x in range(number):
        gitPause(number)

def gitPause(number=0):
    p = '20'

    Key('f2').execute() 
    Pause(p).execute()
    Key('c-c').execute() 
    Pause(p).execute()
    Key('a-tab').execute() 
    Pause(p).execute()
    Key('c-v').execute() 
    Pause(p).execute()
    Key('enter').execute() 
    Pause(p).execute()
    Key('a-tab').execute() 
    Pause(p).execute()
    Key('down').execute() 
    Pause(p).execute()

def dub_click():
    action = Mouse("left:2")
    action.execute()

class GlobalMappings(MappingRule):
    mapping = {  
        # code

        'da': Function(dub_click),
        'move craig <number>': Function(repeat),
        'move craig': Function(gitPause),    
        # Keys
        'plus': Key('plus'),
        'bat': Key('backspace'),
        'bat <number>': Key('backspace:%(number)d'),
        'nip': Key('escape'),
        'Spat': Key('space'),
        'Dink': Key('delete'),
        'down': Key('down'),
        'less than': Text(' <= '),
        'greater than': Text(' >= '),
        'to column': Text('.withColumn("")') + Key('left:2'), 
        'to filter': Text('.filter(col(""))') + Key('left:3'),
        'to equity': Text(' == '),
        'to assignment': Text(' = '),
        'to parens': Text('()'),
        'F call': Text('F.col("")') + Key('left:2'),
        'to select': Text('.select()') + Key('left:1'),
        'to join': Text('.join()') + Key('left:1'),
        'to distinct': Text('.distinct()'),
        'to sort': Text('.sort(col(""))') + Key('left:3'),
        'to not know': Text('.isNotNull()'),
        'to know': Text('.isNull()'),
        'to display': Text('.display()'),
        'two is in': Text('.isin()') + Key('left:1'),
        'to group by count': Text('.groupBy("").agg(count("*"))') + Key('left:18'),


        # '': Text(' '),
        # '': Text(' '),
        # '': Text(' '),
        # '': Text(' '),

		'find <text>': Key("c-f") + Text("%(text)s"),
		'find': Key("c-f"),
        'Dunk': Key('s-delete'), 
        'snap': Key('a-tab'),
        'snap hold': Key('alt:down, tab'),
        'pick': Key('enter,alt:up'),
        'slap': Key('c-tab'),
        'down <number>': Key('down:%(number)d'),
        # 'up': Key('up'),
        'up <number>': Key('up:%(number)d'),
        'law': Key("pgup"),
        'raw': Key("pgdown"),
        'ga': Key("enter"),
        'Back tab': Key('s-tab'),
        'left [<number>]': Key('left:%(number)d'),
        'left dub <number>': Key("ctrl:down, left:%(number)d, ctrl:up"),
        'right [<number>]': Key('right:%(number)d'),
        'right dub <number>': Key("ctrl:down, right:%(number)d, ctrl:up"),
        "cam <camel_text>": Text("%(camel_text)s"),
        "low <lowtext>": Text("%(lowtext)s"),
        "hype <dashtext>": Text("%(dashtext)s"),
        "snake<snaketext>": Text("%(snaketext)s"),
        "dot<dottext>": Text("%(dottext)s"),
        "frame <snaketext>": Text("%(snaketext)s") + Text("_df"),
        "new frame <snaketext>": Text("%(snaketext)s") + Text(R"_df = ") + Text("%(snaketext)s") + Text(R"_df"),
        "double hype <dashtext>": Key("hyphen") + Text("%(dashtext)s"),
        "cal [<pascaltext>]": Text("%(pascaltext)s"),
        "title [<titletext>]": Text("%(titletext)s"),
        'select down <number>': Key("home, shift:down, down:%(number)d, up, end, shift:up"),
        'select up <number>': Key("end, shift:down, up:%(number)d, down, home, shift:up"),
        'select right <number>': Key("ctrl:down, shift:down, right:%(number)d, ctrl:up, shift:up"),
        'select left <number>': Key("ctrl:down, shift:down, left:%(number)d, ctrl:up, shift:up"),
        'select end': Key('s-end'),
        'select home': Key('s-home'),
        'copy end': Key('s-end,c-c'),
        'copy home': Key('s-home, c-c'),
        'select all': Key("c-a"),
        'copy all': Key("c-a,c-c"),
        'line end': Key("end"),
        'line end <number>': Key("end") + Key("left:%(number)d"),
        'line home': Key("home"),
        'line home <number>': Key("home") + Key("right:%(number)d"),
        'undo': Key("c-z"),
        'undo <number>': Key("c-z:%(number)d"),
        'redo ': Key("c-y"),
        'redo <number>': Key("c-y:%(number)d"),
        'win up': Key('win:down, up, win:up'),
        'win right': Key('win:down, right, win:up'),
        'win down': Key('win:down, down, win:up'),
        'win left': Key('win:down, left, win:up'),
        'win search': Key('win:down, s, win:up'),
        'win snip': Key('win:down, s-s, win:up'),
        'copy': Key('c-c'),
        'cut': Key('c-x'),
        'paste': Key('c-v'),
        'del': Key('del'),
        'quotes': Key('dquote'),
        'comma': Key('comma'),
        'snooze': Key('csa-slash'),
        'snap load': Key('w-4') + Pause("10") + Key('c-1') + Pause("10") + Key('f5') + Pause("10") + Key('a-tab'),
        
        'to files': Key("w-1"),
        'to Teams': Key("w-2"),
        'to Web': Key("w-3"),
        'to py': Key("w-4"),
        'to code': Key("w-5"),
        'to VS': Key("w-6"),
        'to excel': Key("w-7"),
        'to bricks': Key("w-8"),
        'to data': Key("w-9"),
        'to kindle': Key("w-0"),
        'run it': Key("c-enter"),
        
        ##############################
        # passwords
        ##############################
        # 'craig pass': Text(craig_pass),
        # 'in pass': Text(in_pass),
        # 'Prod pass': Text(prod_pass),
        # 'Sand pass': Text(sand_pass),
        # 'test pass': Text(testy_pass),
        'in email': Text("csalzsieder@inspirato.com"),
        'in User': Text("csalzsieder"),

        # py spark text
        'show me': Text('.show()') + Key('enter'),
        'count me': Text('.count()') + Key('enter'),
        'print schema': Text('.printSchema()') + Key('enter'),
        # 'log schema': Text('.printSchema()') + Key('enter'),
        "log <snaketext> ": Text('print(') + Text("%(snaketext)s") + Text("_df.count())") + Key('enter') + Text('display(') + Text("%(snaketext)s") + Text("_df)"),
        "count <snaketext> ": Text("%(snaketext)s") + Text("_df.count()book 2") + Key('enter'),
        "display <snaketext> ": Text('display(') + Text("%(snaketext)s") + Text("_df)"),
        "show <snaketext> ": Text("%(snaketext)s") + Text("_df.show()") + Key('enter'),


        'open dock' : Key('win,s') + Pause('20') + Text('docker') + Pause('20') + Key('enter'), 
        '[<number>] tab': Key('tab:%(number)d'),

        # Temporary
        'flag it': Text("# TODO: "),

        #postman
        'Post run': Key("w-8") + Pause('50') + Key("c-enter") + Pause('50') + Key("a-tab")
        }

    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("camel_text").camel(),
        Dictation("snaketext").lower().replace(" ", "_"),
        Dictation("dottext").lower().replace(" ", "."),
        Dictation("dashtext").lower().replace(" ", "-"),
        Dictation("lowtext").lower(),
        Dictation("pascaltext").title().replace(" ", ""),
        Dictation("titletext").title().replace(" ", " "),
        Dictation("text"),
    ]

grammar=Grammar('Global')
grammar.add_rule(GlobalMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

