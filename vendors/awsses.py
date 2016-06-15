class AWSSES(object):
    def getPrice(self, numberofemails):
        #first 62000 free
        if numberofemails <= 62000:
            return 0
        originalnumber = numberofemails
        numberofemails = numberofemails - 62000
        #Email messages are charged at $0.10 per 1,000.
        return round(.1 * numberofemails/1000, 0)
