import discord
from .callbacks import *




class Page(discord.ui.View):    

    necessaryThings = {
        "button":["label","type","callback"],
        "select":["placeholder","options","callback"],
        "options":["label","value"]
    }
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
                for important in self.necessaryThings["button"]:
                    if important not in innerKeys:
                        raise Exception("Missing key in a button: "+important)

                styleVal = getattr(discord.ButtonStyle, key["type"])
                button = discord.ui.Button(style=styleVal, label=key["label"])
                button.callback = retCallback(key["callback"])
                super().add_item(button)

            elif key.startswith("select"):
                key = pageUI[key]
                innerKeys = list(key.keys())

                for important in self.necessaryThings["select"]:
                    if important not in innerKeys:
                        raise Exception(f"Missing key in a select: "+important)

                optionsList = []
                for options in key["options"]:
                    innerKeys = list(options.keys())
                    for important in self.necessaryThings["options"]:
                        if important not in innerKeys:
                            raise Exception(f"Missing key in a select option: "+important)

                    optionsList.append(discord.SelectOption(**options))

                select = discord.ui.Select(placeholder=key["placeholder"], options=optionsList)
                select.callback = retCallback(key["callback"])
                super().add_item(select)

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


        