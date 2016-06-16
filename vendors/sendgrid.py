class SendGrid(object):
    def getPrice(self, numberofemails):
        #0-40000 on 9.95
        if (numberofemails <= 40000):
            return 9.95

        return min( self.planEssentials40(numberofemails), self.planEssentials100(numberofemails),
                    self.planPro100(numberofemails), self.planPro300(numberofemails))

    def planEssentials40(self, numberofemails):
        price = 9.95
        limit = 40000
        overage = .0010
        return self._price(price, limit, overage, numberofemails)

    def planEssentials100(self, numberofemails):
        price = 19.95
        limit = 100000
        overage = .00075
        return self._price(price, limit, overage, numberofemails)

    def planPro100(self, numberofemails):
        price = 79.95
        limit = 100000
        overage = 0.00085
        return self._price(price, limit, overage, numberofemails)

    def planPro300(self, numberofemails):
        price = 199.95
        limit = 300000
        overage = 0.0005
        return self._price(price, limit, overage, numberofemails)


    def _price(self, price, limit, overage, numberofemails):
        surcharge = 0
        if numberofemails > limit:
            surcharge = (numberofemails - limit) * overage
        return price + surcharge
