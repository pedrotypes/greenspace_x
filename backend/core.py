from mongoengine import *
import random


class Player(Document):
    name = StringField(required=True)


class Base(Document):
    name = StringField(required=True)
    size = IntField(default=50)
    x = IntField()
    y = IntField()

    def rollSize(self):
        roll = random.randint(1, 10)
        return roll


class Fleet(Document):
    player = ReferenceField(Player, dbref=False)
    size = IntField(default=10)
    position = ReferenceField(Base, dbref=False)
    destination = ReferenceField(Base, dbref=False)
    eta = IntField(default=0)
    eta_total = IntField(default=0)

    def moveTo(self, base):
        if (base != self.position):
            self.destination = base
            self.eta_total = 3
            self.eta = 3
            self.save()

    def move(self):
        if (self.eta > 0):
            self.eta -= 1
            if (self.eta == 0):
                self.position = self.destination
                self.destination = None
            self.save()
