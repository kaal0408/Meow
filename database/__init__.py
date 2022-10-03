import os
import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from Meow import MONGO_DB


mongodb = MongoClient(MONGO_DB)


try:
    mongodb.server_info()
except ConnectionFailure:
    logging.error("Invalid Mongo DB URL. Please Check Your Credentials! Astro2.0 is Exiting!")
    quit(1)



dtbs = mongodb["app"]
