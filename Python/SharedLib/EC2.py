import boto3
import AWSKey

class EC2:
    def __init__(self):
        key = AWSKey.AWSKey()
        self.session = boto3.Session(
            aws_access_key_id=key.getData()['AWSAccessKeyId'],
            aws_secret_access_key=key.getData()['AWSSecretKey'],
            region_name=key.getData()['region']
        )

    def getSession(self):
        return self.session

if __name__=="__main__":
    test = EC2()
    print(test.getSession())
