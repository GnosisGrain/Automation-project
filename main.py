# This is the template code for the CNE335 Final Project
# Doc McDowell
# CNE 335 Fall

from Server import Server

def print_program_info():
    print("Server Automator v0.1 by Doc McDowell")


if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    my_server_ip = "34.219.44.249"
    my_rsa_key_file = r"C:\Users\Doc\.ssh\DocRootwork.ppk"
    username = "ec2-user"
    my_upgrade_command = 'sudo apt update && sudo apt upgrade -y'
    my_server = Server(my_server_ip, my_rsa_key_file, username, my_upgrade_command)
    print(my_server.ping())
    print("Updating server")
    ssh_result = my_server.upgrade()
    print(''.join(ssh_result))

