from paramiko import SSHClient
from scp import SCPClient
import paramiko
import api_keys
import shutil
import datetime
import os
import sys

host = api_keys.host
port = api_keys.port
user = api_keys.user
passwd = api_keys.passwd
key_file = ""
file_path = api_keys.origin_path
dest_path = api_keys.dest_path


def copytree(src, dst, extension='', copydir=False, symlinks=False, ignore=None):

    for item in os.listdir(src):

        s = os.path.join(src, item)
        d = os.path.join(dst, item)

        if os.path.isdir(s) and copydir:
            shutil.copytree(s, d, symlinks, ignore)

        elif not item.startswith("."):

            if extension and item.endswith(extension):
                if not os.path.exists(dst):
                    os.makedirs(dst)
                shutil.copy2(s, d)

            elif not extension:
                if not os.path.exists(dst):
                    os.makedirs(dst)
                shutil.copy2(s, d)


if __name__ == '__main__':

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f"Conectando ao host: {host} Porta: {port} Usuario: {user} Senha: {passwd}")

    try:
        ssh.connect(host, port=port, username=user, password=passwd)
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(-1)

    with SCPClient(ssh.get_transport(), sanitize=lambda x: x) as scp:

        try:
            scp.get(remote_path=file_path, local_path=dest_path)
        except Exception as e:
            print(e)

    dest_dir = datetime.datetime.now().strftime("%Y-%m-%d")

    print(f"Realiando copia para pasta diária: {dest_dir}")

    copytree(dest_path, dest_dir)

    print("fim")