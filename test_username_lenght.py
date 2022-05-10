import logging


class TestRegistration:
    log = logging.getLogger('[Registration]')

    """ 
    1. Create driver
    2. Open start page
    3. Clear Username field
    4. Fill Username field with no more than 2 any characters
    
    
    """

    def test_username_lenght(self):
