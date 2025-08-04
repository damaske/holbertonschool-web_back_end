#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

from pymongo import MongoClient

if __name__ == "__main__":
    # Подключение к локальному MongoDB
    client = MongoClient()
    nginx_collection = client.logs.nginx

    # Общее количество логов
    log_count = nginx_
