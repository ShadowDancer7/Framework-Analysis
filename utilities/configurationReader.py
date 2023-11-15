from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("C:/Users/Shado/Documents/Framework_Analysis_10/virtual_env/configurations/config.ini")
    return config.get(category, key)
