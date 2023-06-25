from typing import overload


class PlayerInventory:
    main = None
    armor = None
    offHand = None
    selectedSlot = None

    def clear(self):
        ...

    def contains(self, stack):
        ...

    def dropAll(self):
        ...

    def dropSelectedItem(self, entireStack):
        ...

    def getArmorStack(self, slot):
        ...

    def getEmptySlot(self):
        ...

    def getMainHandStack(self):
        ...

    def getSlotWithStack(self, stack):
        ...

    def getStack(self, slot):
        ...

    def indexOf(self, stack):
        ...

    @overload
    def insertStack(self, slot, stack):
        ...

    @overload
    def insertStack(self, stack):
        ...

    def isEmpty(self):
        ...

    def removeOne(self, stack):
        ...

    @overload
    def removeStack(self, slot, amount):
        ...

    @overload
    def removeStack(self, slot):
        ...

    def setStack(self, slot, stack):
        ...
