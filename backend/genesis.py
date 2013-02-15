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
    # StarCraft
    'Aiur',
    'Antiga',
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
    'Roxana',  # <3
    # Star Wars
    # 'Ablajeck',
    # 'Abregado',
    # 'Abrion',
    # 'Allied Tion',
    # 'Ansuroer',
    # 'Antemeridian',
    # 'Anthos',
    # 'Aparo',
    # 'Arkanis',
    # 'Atrivis',
    # 'Auril',
    # 'Altyr',
    # 'Bajic',
    # 'Bestine',
    # 'Bespin',
    # 'Bormea',
    # 'Bothan',
    # 'Bothawui',
    # 'Brak',
    # 'Braxant',
    # 'Byss',
    # 'Cadavine',
    # 'Castell',
    # 'Cerea',
    # 'Chommell',
    # 'Corporate',
    # 'Corellia',
    # 'Coruscant',
    # 'Dalonbian',
    # 'Darpa',
    # 'Dagobah',
    # 'Dantooine',
    # 'Doldur',
    # 'Dromund Kaas',
    # 'Duro',
    # 'Dorval',
    # 'Falleen',
    # 'Farlax',
    # 'Gamorr',
    # 'Gordin Reach',
    # 'Gricho',
    # 'Halla',
    # 'Hapes',
    # 'Haruun Kal',
    # 'Hutta',
    # 'Hypori',
    # 'Illum',
    # 'Juvex',
    # 'Kalarba',
    # 'Kalee',
    # 'Kastolar',
    # 'Kathol',
    # 'Kessel',
    # 'Kuat',
    # 'Korriban',
    # 'Kor-uj',
    # 'Lahara',
    # 'Lytton',
    # 'Maramere',
    # 'Malastare',
    # 'Mandalore',
    # 'Mayagil',
    # 'Meridian',
    # 'Metalorn',
    # 'Moddell',
    # 'Mon Calamari',
    # 'Muunilinst',
    # 'Mygeeto',
    # 'Nal Hutta',
    # 'Nar Shadda',
    # 'Nilgaard',
    # 'Ord Mantell',
    # 'Orus',
    # 'Periphery',
    # 'Quelli',
    # 'Quence',
    # 'Raioballo',
    # 'Rhen Var',
    # 'Rishi',
    # 'Senex',
    # 'Sern',
    # 'Sesswenna',
    # 'Sluis',
    # 'Spar',
    # 'Subterrel',
    # 'Sulorine',
    # 'Taanab',
    # 'Tatooine',
    # 'Tapani',
    # 'Tharin',
    # 'Thisspias',
    # 'Tion Cluster',
    # 'Tython',
    # 'Vivenda',
    # 'Wyl',
    # 'Xappyh',
    # 'Yaga-Minor',
    # 'Apatros',
    # 'Raxus Prime',
    # 'Helo Prime'
]
bases = []
grid = []


def rollCoords(grid):
    x = random.randint(1, 50)
    y = random.randint(1, 30)
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
