class PostmarkApp(object):
    def getPrice(self, numberofemails):
        if numberofemails == 0:
            return 0
        plans = [
            self._price(1000, .0015, numberofemails), #1000 for 1.5pm
            self._price(500000, .001, numberofemails), #500k for 1pm
            self._price(1000000, .00075, numberofemails), #1mm for .75pm
            self._price(2000000, .0005, numberofemails), #2mm for .50pm
            self._price(5000000, .00025, numberofemails), #5mm for .25pm
        ]

        return min( filter(None, plans) )

    def _price(self, minimum, cpe, numberofemails):
        if numberofemails < minimum:
            return False
        else:
            return round(numberofemails * cpe, 2)
