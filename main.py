import paramiko
from io import StringIO


mykey = paramiko.RSAKey.from_private_key_file("bhost")

HOST = '200.106.174.154'
USER = 'ubuntu'
SSHKEY = 'C:\keypairs\bhost'

#Comentario
client = paramiko.SSHClient()
client.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
    
client.connect(hostname=HOST, username=USER, allow_agent=False, look_for_keys=False, pkey=mykey)
stdin, stdout, stderr = client.exec_command("uptime")
   
result = stdout.read().decode()
   
print(result)