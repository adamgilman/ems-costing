class MailGun(object):
    def getPrice(self, numberofemails):
        numberofemails = max(numberofemails - 10000, 0)
        tier1 = min(numberofemails, 500000) * .0005

        numberofemails = max(numberofemails - 500000, 0)
        tier2 = min(numberofemails, 1000000) * .00035

        numberofemails = max(numberofemails - 1000000, 0)
        tier3 = min(numberofemails, 5000000) * .00015

        numberofemails = max(numberofemails - 5000000, 0)
        tier4 = numberofemails * .00010

        return tier1 + tier2 + tier3 + tier4
