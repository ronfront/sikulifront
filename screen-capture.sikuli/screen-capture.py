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
        if exists("1379707447142.png"):
            click(Pattern("1379707447142.png").targetOffset(0,-2))
        elif exists("1379707470322.png"):
            click("1379707470322.png")
        else:
            click("1379707492167.png")
            type("n", KeyModifier.CMD + KeyModifier.SHIFT)
    
    def change_url(self, text):
        type("l", KeyModifier.CMD) 
        type(text + Key.ENTER)
        wait("1379707599945.png")
        wait("1379707510263.png")


#  ----------------------------------

chrome = Chrome()
chrome.active_incognito()
chrome.close_developer_tools()
chrome.change_url("www.google.com")


resize = ["1379708197381.png", ]

for i in xrange(4):
    type(Key.DOWN, KeyModifier.CMD)
    wait("1379702587714.png")

    type(str(i+1))
    type(Key.ESC)

    if i == 3:
        chrome.open_developer_tools(orientation="vertical")
        chrome.close_developer_tools()