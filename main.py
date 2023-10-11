import paramiko



def run_ssh_command(hostname, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode('utf-8')
    client.close()
    return output



hostname = 'example.com'
username = 'your_username'
password = 'your_password'


output = run_ssh_command(hostname, username, password, 'echo "Connection Successful"')
print(output)

output = run_ssh_command(hostname, username, password, 'mkdir test_directory')
print(output)


output = run_ssh_command(hostname, username, password, 'cd test_directory')
print(output)


output = run_ssh_command(hostname, username, password, 'touch test_file.txt')
print(output)


output = run_ssh_command(hostname, username, password, 'ls test_file.txt')
print(output)
