#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Function)

def repeat(number):
    s = 'cd '
    for i in range(0, number):
            s += '../'
    
    Text('{}'.format(s)).execute()

class CodeMappings(MappingRule):
    mapping = {  
            # Shortcuts
            'previ': Key('cs-tab'),
		    'nexty': Key('c-tab'), 
		    'open tab': Key('sa-1'), 
		    'close tab': Key('c-w'), 
		    'kill it': Key('c-c'), 
		    'exit': Text('exit') + Key('enter'), 
		    'build Wheel': Text('buildWheel.sh') + Key('enter'), 
		    'load Wheel': Text('loadWheelToCluster.sh') + Key('enter'), 
		    'again': Key('up,enter'), 
		    'back <number>': Function(repeat) + Key('enter'),
            'list': Text('ls') + Key('enter'),
            'cd <lowtext>': Text('cd %(lowtext)s') + Key('enter'),
            'cd passlist': Text('cd workspace/passlist') + Key('enter'),
            'cd source': Text('cd gitprojects/data-pipeline/workspace/passlist') + Key('enter'),
            
            # Commands

            # docker
            'dock list': Text('docker ps -a') + Key('enter'),
            'dock rem': Text('docker rm'),
            'dock start': Text('docker start'),
            'dock stop': Text('docker stop'),
            'dock logs': Text('docker logs'),
            'dock compose': Key('sa-1') + Pause('200') + Text('docker-compose up') + Key('enter'),
            'dock to red': Text('docker exec -it redis sh') + Key('enter'),
            'dock red': Text('docker run --name redis -p 6379:6379 -d redis') + Key('enter'),
            'dock start red': Text('docker start redis') + Key('enter'),

            #redis
            'b <number>': Text('b %(number)d') + Key('enter'),
            'red mem': Text('smembers'),
            'red mon': Text('monitor'),
            'red commander': Text('redis-commander') + Key('enter'),
            'red Klee': Text('redis-cli'),
            'red stat': Text('memory stats') + Key('enter'),
            'red info': Text('info') + Key('enter'),
            'red <number>': Text('select %(number)d') + Key('enter'),
            'red qa': Text('rdcli -h redis-passlist-shared-qa.redis.cache.windows.net -p 6379 -a e1JGBeEZQcdlbsMqa1E034HWwa2bR5IwfxwhEqJ5LFc=') + Key('enter'),
            'red test': Text('rdcli -h redis-passlist-shared-test.redis.cache.windows.net -p 6379 -a NR9PB8lw9O77+Ev5HRsNC9HMkq2Rruku4LduKRCnYuU=') + Key('enter'),
        }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("text"),
        Dictation("lowtext", default="").lower(), 
    ]

context = AppContext(executable=R'C:\Users\csalzsieder\Downloads\cmder\vendor\conemu-maximus5\ConEmu64.exe')
grammar=Grammar('Shell',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None