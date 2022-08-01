# UIMaker
A simple tool for creating a discord bot UI from just JSON!

**NOTE: This is for quick prototyping, this is like the bootstrap of discord ui, you CAN use it for actual bots, but as of rn its under development**

# Setup
`pip install -U git+https://github.com/SemiConductorShortage/UIMaker`

Supports:

Embeds
- The embeds can have a hex color code like so "#ff0000"
- The embeds can have either "color" or "colour", you arent forced to use a certain spelling now :sunglasses:

Buttons
- The buttons can have a callback, but you must first define the callback, you can do that in a class that inherits UIMaker.Callbacks
```py
class MyCallbacks(UIMaker.Callbacks):
    async def callbackForButton(interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")
    async def callbackForAnotherButton(interaction: discord.Interaction):
        await interaction.response.send_message("Hello again!")
```

and then in the json, simply place `"callback":"callBackForButton"` in the button section

You can only have a single embed in the message as discord only allows that much per bot
This can be bypassed with a webhook but the goal of this project isnt to find workarounds for the API

Docs : [WIP]
