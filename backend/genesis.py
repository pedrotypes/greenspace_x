from mongoengine import *
from core import *

connect('stargame')


# Player
Player.drop_collection()
player = Player(name='Teh Pwnerer')
player.save()

# Bases
Base.drop_collection()
names = [
    'Aiur',
    'Antiga Prime',
    'Braxis',
    'Char',
    'Chau Sara',
    'Feronis',
    'Gantris',
    'Helios',
    'Korhal',
    'Lorcadia',
    'Mar Sara',
    'Moria',
    'New Folsom',
    'Pegasus',
    'Pridewater',
    'Raydin',
    'Redstone',
    'Roxara',
    'Shakuras',
    'Tarsonis',
    'Umoja',
    'Vyctor',
    'Xil',
    'Ynoth',
    'Zhakul',
]
bases = []
for n in names:
    b = Base(name=n)
    b.size = b.rollSize()
    b.save()
    bases.append(b)
    print "%s (%d)" % (b.name, b.size)

# Fleets
Fleet.drop_collection()

f = Fleet(player=player, position=bases[0])
f.moveTo(bases[-1])
print "Fleet moving from %s to %s" \
    % (f.position.name, f.destination.name)
