import os
class conf:
    host = "localhost"
    database = "sandwich_maker_api"
    port = 3306
    user = "root"
    password = os.environ.get("MYSQL_PASSWORD", "")