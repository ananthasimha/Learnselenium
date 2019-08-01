import logging

class LogGen():
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C://Users//ashankara//PycharmProjects//Pytest//logs//automations.log",level=logging.INFO,
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %P')
        logger=logging.getLogger()

        return logger