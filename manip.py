# requirements.txt from this project
# 1. method 1: analyze env/venv
# python -m pip freeze > requirements.txt
# 2. methode2: analyze project
# pipreqs --force pathproject


# import tchatbot
# x = tchatbot.f(3)

# import tchatbot as tc
# x = tc.f(3)

from tchatbot import f, g

import tchat.training.dataset as dts
import tchat.training.train as tr
import tchat

# import package numpy => + sous package et modules
import numpy as np

t = np.zeros((10,10))
data = np.random.normal(10, 4, 100)

x = f(3) + g(4)
# use h from tchat.training.dataset as dts
# and same function h from tchat
y = x + dts.h(x) + tr.i(x) + tchat.h(x)

print(x, y)

