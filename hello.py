# Define a simple hello function
def hello(name):
    return "Hello {} have a woderful day.".format(name)

def night(name):
    return "Hello {} have a woderful night.".format(name)

name = (input('Enter your name:\n'))

print(hello(name))
print(night(name))
