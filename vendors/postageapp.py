class PostageApp(object):
    def getPrice(self, numberofemails):
        #0-40000 on 9.95
        if (numberofemails <= 10000):
            return 9

        plans = [
            self._price(9, 10000, .0010, numberofemails),    #pigeon
            self._price(29, 40000, .0010, numberofemails), #falcon
            self._price(79, 100000, .00075, numberofemails), #owl
            self._price(199, 400000, .00075, numberofemails), #eagle
        ]
        return min( plans )

    def _price(self, price, limit, overage, numberofemails):
        surcharge = 0
        if numberofemails > limit:
            surcharge = (numberofemails - limit) * overage
        return round(price + surcharge, 2)
