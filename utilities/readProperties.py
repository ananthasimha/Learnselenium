import configparser

config=configparser.RawConfigParser()
config.read('.\\Configuration\\config.ini')

class ReadConfig():
    @staticmethod
    def getApplicationUrl():
        url=config.get('Login Details','baseurl')
        return url
    @staticmethod
    def getUsername():
        Username=config.get('Login Details','Username')
        return Username
    @staticmethod
    def getPassWord():
        PassWord=config.get('Login Details','PassWord')
        return PassWord



