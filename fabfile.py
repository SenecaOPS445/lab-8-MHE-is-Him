from fabric import Connection

# Define the host and port
host = "student@myvmlab.senecapolytechnic.ca"
port = 7305

# Create the connection object
conn = Connection(host=host, port=port)

# Task 1: Gather system facts (using Ansible command via SSH)
def facts_gather():
    result = conn.run('ansible -m setup localhost', hide=True)
    print(result.stdout)

# Task 2: Ensure the system is up to date
def system_update():
    conn.sudo('yum update -y')

# Task 3: Install git package
def git_install():
    conn.sudo('yum install -y git')

# Task 4: Ensure SSH service is running
def ssh_ensure():
    conn.sudo('systemctl start sshd')
    conn.sudo('systemctl enable sshd')

# Running the tasks
facts_gather()
system_update()
git_install()
ssh_ensure()
