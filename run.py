import os


data = ""

with open('rollbar-agent.conf', 'r') as conf:
    data = conf.read().replace('${ACCESS_TOKEN}', os.environ.get('ACCESS_TOKEN', ''))
    data = data.replace('${ENVIRONMENT}', os.environ.get('ENVIRONMENT', ''))
    data = data.replace('${PATH_TO_ROOT}', os.environ.get('PATH_TO_ROOT', ''))
    conf.close()

with open('rollbar-agent.conf', 'w+') as conf:
    conf.write(data)
    conf.close()

os.system('python rollbar-agent')