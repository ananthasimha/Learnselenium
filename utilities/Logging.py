import logging

class LogGen():
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automations.log",format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%y %I:%M:%S %P')
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger