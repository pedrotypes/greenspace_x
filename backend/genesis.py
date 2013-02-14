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
grid = []


def rollCoords(grid):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    return [x, y]

for n in names:
    coords = rollCoords(grid)
    b = Base(name=n, x=coords[0], y=coords[1])
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
