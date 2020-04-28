import logging

'''
Here we can configure our logging the way we want
'''
class LogInfo:
    log_file = None

    def __init__(self, log_file):
        self.log_file = log_file
        self.configureLogging(log_file)

    def configureLogging(self, log_file):
        # Log Information
        # set up logging to file - more info here https://docs.python.org/3/library/logging.html#logging.basicConfig
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename=log_file,
                            filemode='w')
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)  # we can specify what level or above goes into the console
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(asctime)s %(name)-7s: %(levelname)-7s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)


'''
Reference:
https://docs.python.org/3/howto/logging-cookbook.html
https://docs.python.org/3/howto/logging.html
'''