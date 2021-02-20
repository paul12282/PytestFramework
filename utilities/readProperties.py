import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getUrl():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getEmail():
        valid_email = config.get('common info', 'email')
        return valid_email

    @staticmethod
    def getInvalidemail():
        invalid_email = config.get('common info', 'invalid_email')
        return invalid_email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getSearch():
        search = config.get('common info', 'search')
        return search

    @staticmethod
    def getInvalidSearch():
        invalid_search = config.get('common info', 'invalid_search')
        return invalid_search