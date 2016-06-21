class CritSend(object):
    def getPrice(self, numberofemails):
        if numberofemails == 0:
            return 0
        plans = [
            self._price(0, .0005, numberofemails), #1000 for 1.5pm
            self._price(500000, .0005, numberofemails), #500k for 1pm
            self._price(3000000, .00033, numberofemails), #1mm for .75pm
            self._price(10000000, .0003, numberofemails), #2mm for .50pm
            self._price(50000000, .00028, numberofemails), #5mm for .25pm
        ]

        return min( [p for p in plans if p is not False])

    def _price(self, minimum, cpe, numberofemails):
        if numberofemails < minimum:
            return False
        else:
            return round(numberofemails * cpe, 2)
