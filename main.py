from paramiko import SSHClient
from scp import SCPClient
import paramiko
import api_keys

host = api_keys.host
port = api_keys.port
user = api_keys.user
passwd = api_keys.passwd
key_file = ""
file_path = api_keys.origin_path
dest_path = api_keys.dest_path


if __name__ == '__main__':

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=user, password=passwd)

    with SCPClient(ssh.get_transport(), sanitize=lambda x: x) as scp:

        try:
            scp.get(remote_path=file_path, local_path=dest_path)
        except Exception as e:
            print(e)
