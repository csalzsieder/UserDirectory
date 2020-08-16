#imports the library
# from pywinauto.application import Application
from dragonfly import (BringApp, StartApp, Function, Mimic, Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mouse)
from passes import prod_pass, sand_pass, craig_pass, in_pass

def start_day():
    # Mimic('open', 'dryfly')
    # Pause('500')
    Mimic('open', 'pie')
    Mimic('connect', 'pre')

def connect_pre():
    StartApp(R"C:\Program Files (x86)\Pritunl\pritunl.exe").execute()
    Pause("500").execute()
    Mouse("(0.92, 0.1), left").execute()
    Pause('100').execute()
    Mouse("(0.92, 0.1), left").execute()
    Pause('400').execute()
    Text(sand_pass).execute()
    Pause('50').execute()
    Mouse("(0.75, 0.1), left").execute()

def connect_cisco():
    StartApp(R"C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\vpnui.exe").execute()
    Pause("100").execute()
    Mouse("(0.85, 0.5), left").execute()
    Pause("100").execute()
    Text(in_pass).execute()
    Key('enter').execute()

class GlobalMappings(MappingRule):
    mapping = {  
        'connect cisco': Function(connect_cisco),
		'find [<text>]': Key("c-f") + Pause("10") + Text("%(text)s"),
        'back space': Key('backspace'),
        'nip': Key('escape'),
        'Spat': Key('space'),
        'Dink': Key('delete'),
        'snap': Key('a-tab'),
        'snap hold': Key('alt:down, tab'),
        'pick': Key('enter,alt:up'),
        'slap': Key('c-tab'),
        'down': Key('down'),
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
        "cam [under] <camel_text>": Text("%(under)s%(camel_text)s"),
        "snake [<under>] <snaketext>": Text("%(under)s%(snaketext)s"),
        "low <lowtext>": Text("%(lowtext)s"),
        "dash [<dash>] <dashtext>": Text("%(dash)s%(dashtext)s"),
        "skull [<pascaltext>]": Text("%(pascaltext)s"),
        "title [<titletext>]": Text("%(titletext)s"),
        'select down <number>': Key("home, shift:down, down:%(number)d, up, end, shift:up"),
        'select up <number>': Key("end, shift:down, up:%(number)d, down, home, shift:up"),
        'select right <number>': Key("ctrl:down, shift:down, right:%(number)d, ctrl:up, shift:up"),
        'select left <number>': Key("ctrl:down, shift:down, left:%(number)d, ctrl:up, shift:up"),
        'select all': Key("c-a"),
        'copy all': Key("c-a,c-c"),
        'line end [<number>]': Key("end") + Key("left:%(number)d"),
        'line home [<number>]': Key("home") + Key("right:%(number)d"),
        'undo': Key("c-z"),
        'undo [<number>]': Key("c-z:%(number)d"),
        'redo ': Key("c-y"),
        'redo [<number>]': Key("c-y:%(number)d"),
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
        'to end': Key('end'),
        'to home': Key('home'),
        'quote': Key('squote'),
        'comma': Key('comma'),
        
        'snap load': Key('w-4') + Pause("10") + Key('c-1') + Pause("10") + Key('f5') + Pause("10") + Key('a-tab'),
        
        'to files': Key("w-1"),
        'to mail': Key("w-2"),
        'to Teams': Key("w-3"),
        'to Web': Key("w-4"),
        # 'to web': Key("w-4") + Pause('10') + Key("enter"),
        #'to bricks': Key("win:down, 4, 4, win:up") + Pause('50') + Key("enter"),
        # 'to pie': Key("w-5") + Pause('10') + Key("enter"),
        'to py': Key("w-5"),
        'to code': Key("w-6"),
        # 'to code': Key("win:down, 5, 5, win:up") + Pause('50') + Key("enter"),
        # 'to stud': Key("w-7"),
        'to stud': Key("w-7") + Pause('10') + Key("enter"),
        'to study': Key("win:down, 7, 7, win:up") + Pause('50') + Key("enter"),
        
        # 'to studs': Key("win:down, 6, 6, 6, win:up") + Pause('50') + Key("enter"),
        # 'to data': Key("w-7"),
        'to post': Key("w-8"),
        'to shell': Key("w-9"),
        # 'to shell': Key("w-8") + Pause('10') + Key("enter"),
        'to bricks': Key("w-0"),
        # 'to data': Key("w-0"),
        # 'to dragon': Key("w-1,0"),
        # 'to Notepad': Key("w-11"),
        
        ##############################
        # passwords
        ##############################
        'craig pass': Text(craig_pass),
        'in pass': Text(in_pass),
        'Prod pass': Text(prod_pass),
        'Sand pass': Text(sand_pass),
        # 'test pass': Text(testy_pass),
        'in email': Text("csalzsieder@inspirato.com"),
        'in User': Text("csalzsieder"),

        'open pie': StartApp(R"C:\Users\csalzsieder\AppData\Local\Programs\Microsoft VS Code\Code.exe") 
            + Pause('500') + Key("cs-o,a-d") + Key("c-k,c-o,a-d") + Pause('50') 
            + Text(R'C:\NatLink\NatLink\MacroSystem') + Key("enter, tab:8, enter"),
        'open react': StartApp(R"C:\Users\csalzsieder\AppData\Local\Programs\Microsoft VS Code\Code.exe") 
            + Pause('500') + Key("cs-o,a-d") + Key("c-k,c-o,a-d") + Pause('50') 
            + Text(R'D:\GitProjects\react-components') + Key("enter, tab:8, enter"),
        #         "Open dry fly": Key("cs-o,a-d") + Text('D:\GitProjects\dryfly\FreeStone\DryFly.sln') + Key('enter'),
        # "Open MC API": Key("cs-o,a-d") + Text('D:\GitProjects\marketing-content-api\src\MarketingContent.Api.sln') + Key('enter'),
        'connect pre': Function(connect_pre),
        '[<number>] tab': Key('tab:%(number)d'),
        'Start day': Function(start_day),

        # Temporary
        'flag it': Key("enter") + Text("//ToDo: DF-10303 remove unused fields, delete later") + Key("down,c-k,c-c"),

        #postman
        'Post run': Key("w-8") + Pause('50') + Key("c-enter") + Pause('50') + Key("a-tab")

        }

    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("camel_text", default="").camel(),
        # Define a Dictation element that produces snake case text,
        # e.g. hello_world.
        Dictation("snaketext", default="").lower().replace(" ", "_"),
        Dictation("dashtext", default="").lower().replace(" ", "-"),
        Dictation("lowtext", default="").lower(),
        # Define a Dictation element that produces text matching Python's
        # class casing, e.g. DictationContainer.
        Dictation("pascaltext", default="").title().replace(" ", ""),
        Dictation("titletext", default="").title().replace(" ", " "),
        # Allow adding underscores before cased text.
        Choice("under", {"under": "_"}, default=""),
        Choice("dash", {"dash": "-"}, default=""),
        
        Dictation("text")
    ]

grammar=Grammar('Global')
grammar.add_rule(GlobalMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

