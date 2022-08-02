
class empty:
    pass #This class is used to filter out the things that are from a normal class

class Callbacks:
	pass

def retCallback(funcName:str):
    if hasattr(Callbacks, funcName):
        return getattr(Callbacks,funcName)

def RegisterAllCallbacks():
    for obj in Callbacks.__subclasses__():
        funcList = dir(obj)
        for func in funcList:
            if func not in dir(empty):
                setattr(Callbacks, func, getattr(obj,func))