class AWSKey:
    def __init__(self, credFile="../../Secret/AWSKey", configFile="../../Secret/AWSConfig"):
        self.awsKeyFile=credFile
        self.configFile=configFile
        self.data = {}
        with open(self.awsKeyFile, 'r') as fh:
            for line in fh:
                field = line.split('=')
                self.data[field[0]] = field[1]
        with open(self.configFile, 'r') as fh:
            for line in fh:
                field = line.split('=')
                self.data[field[0]] = field[1]

    def getData(self):
        return self.data

