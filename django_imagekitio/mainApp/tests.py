from django.test import TestCase

class imagekitAuthTest():
    
    def __init__(self,token,expire,signature,created=None):

        self.token = token
        self.expire = expire
        self.signature = signature