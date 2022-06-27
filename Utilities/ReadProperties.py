import configparser
config = configparser.RawConfigParser()
config.read("/Users/ticvictech/PycharmProjects/IBS-Automation/Configurations/config.ini")

class Readconfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
         username = config.get('common info', 'username')
         return username

    @staticmethod
    def getPassword():
         password = config.get('common info', 'password')
         return password




