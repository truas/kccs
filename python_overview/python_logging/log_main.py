import logging
import sys
import os
''' 
The line below is used to adjust the relative path of our current main.py to the parent folder. 
    We are basically setting up the PYTHONPATH. That way, when Python looks for the package it will find it.
If you are using an IDE you don't have to worry about it, almost of them do this automatically.
However, via command line  you can either:
    1. Include the the path to your module in PYTHONPATH;
    2. Use the line below to set the new path. It is important do to this before the import from other 
    packages and scripts you are importing in your program.
'''
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

'''
One of the best ways to setup a log is to configure it in a separate class
isolated from the actual code
'''
from python_logging.log_setup import LogInfo


# Main block
if __name__ == "__main__":
    logs = LogInfo("log_info.txt") #log filne name -  you can create more
    '''
    We can setup different code areas to specific logger objects
    '''
    """ Application code   1"""
    logger1 = logging.getLogger('myapp.area1')

    """ Application code  2 """
    logger2 = logging.getLogger('myapp.area2')

    '''
    Depending the level of importance of our messages, we can redirect our logs to the common log or create specific files
    Since we have separate areas defined, they are categorized accordingly in our logs
    '''
    logger1.debug('Quick zephyrs blow, vexing daft Jim.')
    logger1.info('How quickly daft jumping zebras vex.')
    logger2.warning('Jail zesty vixen who grabbed pay from quack.')
    logger2.error('The five boxing wizards jump quickly.')
    logger2.info('Info about Logger2 (App2).')
    logger2.debug('Debug info about Logger2 (App2) only available in the log, not the console')

    logger1.debug('Debug me later, debug me now, your code will be... phenomenal?')

    logging.info('Program finished with no errors')
    logging.shutdown()



'''
Reference:
https://docs.python.org/3/howto/logging-cookbook.html
https://docs.python.org/3/howto/logging.html
'''