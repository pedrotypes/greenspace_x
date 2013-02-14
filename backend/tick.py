from mongoengine import *
from core import *
connect('stargame')


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
