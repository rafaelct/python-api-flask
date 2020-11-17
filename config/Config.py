import os

DATABASE_URL = os.environ['DATABASE_URL']
strDb = DATABASE_URL
#strDb = "host=postgresql_container dbname=store user=postgres password=admin"
#expiredToken = 60
expiredToken = 300
