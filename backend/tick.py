from mongoengine import *
from core import *
connect('stargame')


# Increment money on all bases
for base in Base.objects:
    base.tick()
    print "%s has %d money" % (base.name, base.money)

# Decrease ETA on moving ships
for fleet in Fleet.objects(eta__gt=0):
    fleet.move()
    if fleet.eta > 0:
        # Just scooting along... boring
        print "%s (%s) moving closer to %s (eta: %d)" \
            % (fleet.id, fleet.player.name, fleet.destination.name, fleet.eta)
    else:
        # Arriving at destination
        base = fleet.position
        print "%s arrived at %s (eta: %d)" \
            % (fleet.id, base.name, fleet.eta)

        # If destination does't belong to fleet owner, conquer it
        if (base.player != fleet.player):
            base.player = fleet.player
            base.save()
