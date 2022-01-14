from configparser import ConfigParser
import os.path
import sys
from dotenv import load_dotenv

config_object = ConfigParser()

load_dotenv()

host = os.getenv('host')
port = os.getenv('port')
user = os.getenv('user')
passwd = os.getenv('passwd')
origin_path = os.getenv('origin_path')
dest_path = os.getenv('dest_path')

if any(v is None for v in [host, port, user, passwd, origin_path, dest_path]):

#if [x for x in (host, port, user, passwd, origin_path, dest_path) if x is None]:

    if not os.path.isfile("config.ini"):
        print("Check config file config.ini for parameters")

        config_object.add_section('CONFIG')
        config_object.set('CONFIG', 'host', 'xxxx')
        config_object.set('CONFIG', 'port', '22')
        config_object.set('CONFIG', 'user', 'my_user')
        config_object.set('CONFIG', 'passwd', 'xxxxxxx')
        config_object.set('CONFIG', 'origin_path', '.')
        config_object.set('CONFIG', 'dest_path', '.')

        with open(r"config.ini", 'w') as configfile:
            config_object.write(configfile)

        sys.exit()

    config_object.read("config.ini")

    host = config_object['CONFIG']['host']
    port = config_object['CONFIG']['port']
    user = config_object['CONFIG']['user']
    passwd = config_object['CONFIG']['passwd']
    origin_path = config_object['CONFIG']['origin_path']
    dest_path = config_object['CONFIG']['dest_path']
