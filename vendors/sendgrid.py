class SendGrid(object):
    def getPrice(self, numberofemails):
        #0-40000 on 9.95
        if (numberofemails <= 40000):
            return 9.95

        plans = [
            self._price(9.95, 40000, .0010, numberofemails),    #ess40
            self._price(19.95, 100000, .00075, numberofemails), #ess100
            self._price(79.95, 100000, .00085, numberofemails), #pro100
            self._price(199.95, 300000, .0005, numberofemails), #pro300
            self._price(399.95, 700000, .00045, numberofemails), #pro700
        ]
        return min( plans )

    def _price(self, price, limit, overage, numberofemails):
        surcharge = 0
        if numberofemails > limit:
            surcharge = (numberofemails - limit) * overage
        return price + surcharge
