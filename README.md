# Python Script to Copy Files with SCP

This automates the copy of files in a remote server.

You can use wildcards in the origin path, like /home/*.txt

## Configuration

Create a config.ini file or use environmental variables:

```
[CONFIG]
host = 172.168.9.10
port = 22
user = my_user
passwd = my_pass
origin_path = /home/*.dat
dest_path = .
```