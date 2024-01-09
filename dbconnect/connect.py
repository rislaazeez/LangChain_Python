from pymongo import MongoClient


def connect_db(url):
    my_client = MongoClient(url)
    return my_client
