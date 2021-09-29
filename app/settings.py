import os
from params.parameters import Parameters

# Load Environment variables
MESSAGE = os.getenv('MESSAGE')

# Load arguments
opts = Parameters().parse()

name = opts.name