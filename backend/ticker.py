from mongoengine import *
from core import *
import time
connect('stargame')


def main():
    print "Ticker is running..."
    try:
        while True:
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

            # Wait a bit before running again
            time.sleep(0.250)

    except KeyboardInterrupt:
        print "Bye!"


main()
