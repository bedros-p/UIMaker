import discord
def retCallback(funcName:str):
    if hasattr(Callbacks, funcName):
        return getattr(Callbacks,funcName)

class Page(discord.ui.View):    
    def __init__(self,pageUI:dict):
        super().__init__()
        self.pageUI = pageUI
    def Create(self):
        pageUI = self.pageUI
        embed = None
        for key in list(pageUI.keys()):
            if key.startswith("button"):
                key = pageUI[key]
                innerKeys = list(key.keys())
                if "label" not in innerKeys:
                    raise AttributeError("Label not included!")
                if "type" not in innerKeys:
                    raise AttributeError("Type not included!")
                if "callback" not in innerKeys:
                    raise AttributeError("Callback not included!")

                styleVal = getattr(discord.ButtonStyle, key["type"])
                button = discord.ui.Button(style=styleVal, label=key["label"])
                button.callback = retCallback(key["callback"])
                super().add_item(button)

        if "embed" in pageUI:
            print(pageUI)
            modifiedDict = pageUI["embed"]
            if "colour" in modifiedDict:
                modifiedDict["color"] = modifiedDict["colour"]
                del modifiedDict["colour"]

            if isinstance(modifiedDict["color"], str):
                if (modifiedDict["color"].startswith("#")):
                    modifiedDict["color"]=modifiedDict["color"].replace("#",'')
                    modifiedDict["color"]=int(modifiedDict["color"],16)
                
            embed = discord.Embed.from_dict(pageUI["embed"])
        return {
            "embed": embed,
            "view" : self
        }

class empty:
    pass
class Callbacks:
	pass

def RegisterAllCallbacks():
    for obj in Callbacks.__subclasses__():
        funcList = dir(obj)
        for func in funcList:
            if func not in dir(empty):
                setattr(Callbacks, func, getattr(obj,func))
        