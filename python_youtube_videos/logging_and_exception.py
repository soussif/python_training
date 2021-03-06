
import logging
import traceback

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    phrase = "Text"
    translation = ""
    try:
        for letter in phrase:
            if letter in "AEIOUaeiou":
                translation = translation + "g"
    except ValueError as e:
        print("Invalid Input " + e)
    except TypeError as e:
        print("Invalid Input " + e)
    else:
        print("everything is fine")
    finally:
        print("cleanup")
    return greeting



try:
    a = [1, 2, 3]
    value = a[3]
except:
    logging.error("uncaught exception: %s", traceback.format_exc())


name = 'Faek'
lambda arguments: expression
add10 = lambda x: x + 10

def add10_func(x):
    return x+ 10
print(add10(5))
mult = lambda x,y: x*y
print(mult(2,7))

print(greet(name))

import useful_tools
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
logger = logging.getLogger(__name__)
logger.propagate = False
logger.info("hello from logger")
