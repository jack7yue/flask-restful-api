from os import environ


MONGO_SERVICE_NAME = environ['MONGO_SERVICE_NAME'] if 'MONGO_SERVICE_NAME' in environ else None
MONGO_PRIMARY_KEY = '_id'
MONGO_SET = '$set'
MONGO_COUNTER_NAME = 'userid'
MONGO_INCREMENT = '$inc'
MONGO_SEQ = 'seq'


