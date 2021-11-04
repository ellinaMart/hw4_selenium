import random
import string
from model.letter import Letter

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

email_body = random_string("text", 20) + ' ' + random_string("text", 20)