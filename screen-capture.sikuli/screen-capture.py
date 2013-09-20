# NOTE ENSURE DEVELOPER TOOLS ON AND ITS TO MINIMUM SIZE!
# functions

class Chrome:
    def __init__(self):
        pass
    def close_developer_tools(self):
        if exists("1379707301383.png"):
            click(Pattern("1379707301383.png").targetOffset(-35,0))
        
    def open_developer_tools(self, orientation="vertical"):    
        type("i", KeyModifier.CMD + KeyModifier.ALT)
        wait("1379707301383.png")
        if orientation == "vertical" and exists(Pattern("1379707392448.png").exact()):
            click(Pattern("1379707392448.png").exact())
            wait("1379707301383.png")
        elif orientation == "horizontal" and exists(Pattern("1379707984221.png").exact()):
            click(Pattern("1379707984221.png").exact())
            wait("1379707301383.png")

    def active_incognito(self):
        if exists(Pattern("1379707447142.png").exact()):
            click(Pattern("1379707447142.png").exact())
        elif exists("1379707470322.png"):
            click("1379707470322.png")
        else:
            click("1379707492167.png")
            type("n", KeyModifier.CMD + KeyModifier.SHIFT)
    

    def active_regular(self):
        if exists(Pattern("1379710307757.png").targetOffset(-8,-3)):
            click(Pattern("1379710307757.png").targetOffset(-8,-3))
        elif exists(Pattern("1379710195504.png").targetOffset(-11,-12)):
            click(Pattern("1379710195504.png").targetOffset(-11,-12))

    def change_url(self, text):
        type("l", KeyModifier.CMD) 
        type(text + Key.ENTER)
        if exists("1379707599945.png"):
            waitVanish("1379707599945.png")
        wait("1379707510263.png")


#  ----------------------------------

chrome = Chrome()




sites = [
    ["http://storefront-staging.herokuapp.com/", "home", "v0"],
    ["http://storefront-staging.herokuapp.com/about", "about", "v0"],
    ["http://storefront-staging.herokuapp.com/how-it-works", "how-it-works", "v0"],
    ["http://storefront-staging.herokuapp.com/contact", "contact", "v0"],
    ["http://storefront-staging.herokuapp.com/press", "press", "v0"],
    ["http://storefront-staging.herokuapp.com/team", "team", "v0"]]
        

resizers = [
    ["1379708197381.png", "desktop"], 
    ["1379708584510.png", "tabletl"],
    ["1379708595257.png", "tabletp"],
    ["1379708612919.png", "iphonep"]]


for url, handle, version in sites:
    chrome.active_incognito()
    chrome.close_developer_tools()
    chrome.change_url(url)
    
    for resize, platform in resizers:
        # use a key based approach
        # hotkey for window resizer
        saveName = "_".join([handle, platform, version])
        type(Key.DOWN, KeyModifier.CMD)
        wait("1379702587714.png")
    
        click(resize)
    
        # note iPhone requires a google vertical developer
        if resize == "1379708612919.png":
            waitVanish("1379702587714.png")
            chrome.open_developer_tools(orientation="vertical")
    
        # hotkey for awesome screenshot (preset as CMD+Up Arrow)
        type(Key.UP, KeyModifier.CMD)
        wait("1379709490639.png")
        click("1379709478440.png")
    
        # switch to annotate screens 
        chrome.active_regular()
    
        wait("1379710431265.png")
        click("1379710431265.png")
        click("1379710484223.png")
        click("1379710540467.png")
        click(Pattern("1379710582173.png").targetOffset(-21,0))
        click(Pattern("1379712476524.png").targetOffset(-17,-34))
        type("a", KeyModifier.CMD)
        type(Key.DELETE + saveName)
    
        click("1379711280407.png")
        wait("1379711344853.png", 30)        
        type("w", KeyModifier.CMD)
        chrome.active_incognito()
        chrome.close_developer_tools()
 