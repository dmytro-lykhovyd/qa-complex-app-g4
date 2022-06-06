import datetime
import logging
import random
import string
from time import sleep


def random_num():
    """Generate random number"""
    return str(random.randint(100000, 999999))


def random_str(length=6):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def wait_until_ok(timeout: int, period: float):
    """Retries function until ok"""
    logger = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        logger.warning(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_wrapper(func):
    """add logs for method using docstring"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecorator]")
        result = func(*args, **kwargs)
        if len(args) > 1 and isinstance(args[1], User):
            log.info(f"Using profile: {args[1].username}")
        log.info(f"{func.__doc__}")
        return result

    return wrapper


class User:

    def __init__(self, username="", email="", password=""):
        self.username = username if username else f"{random_str()}{random_num()}"
        self.email = email if email else f"{self.username}@random.mail"
        self.password = password if password else f"{random_str(7)}{random_num()}"

    def __str__(self):
        return self.username

