# le module tchat.training.train

# from .dataset import h
from ..common import initCommon
import tchat.training.dataset as dts

def i(x):
    # return h(x)*x
    initCommon()
    return dts.h(x)*x
