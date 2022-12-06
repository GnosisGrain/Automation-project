import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, key_file, username, upgrade_command):
        self.server_ip = server_ip
        self.ping()
        self.server_ip = server_ip
        self.username = username
        self.command = upgrade_command
        self.key_file = key_file

    def ping(self):
        print("The Server IP is", self.server_ip)
        result = os.system("ping -n 5 %s" % self.server_ip)
        return result

    def upgrade(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        k = paramiko.RSAKey.from_private_key_file(self.key_file)
        ssh_client.connect(hostname=self.server_ip, username=self.username, pkey=k)


        stdin, stdout, stderr = ssh_client.exec_command(self.command)

        result = stdout.readlines() + stderr.readlines()

        ssh_client.close()

        return result



