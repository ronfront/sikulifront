# NOTE ENSURE DEVELOPER TOOLS ON AND ITS TO MINIMUM SIZE!
# functions

class Chrome:
    def __init__(self):
        pass
    def close_developer_tools(self):
    
        if exists():
            click()
        
    def open_developer_tools_vertical(self):    
        type("i", KeyModifier.CMD + KeyModifier.ALT)
        wait()
        if exists() and exists():
            click()
            wait()

    def active_incognito(self):
        if exists():
            click()
        elif exists():
            click()
        else:
            click()
            type("n", KeyModifier.CMD + KeyModifier.SHIFT)
    
    def change_url(self, text):
        type("l", KeyModifier.CMD) 
        type(text + Key.ENTER)
        wait()
        wait()


#  ----------------------------------

chrome = Chrome()
chrome.active_incognito()
chrome.close_developer_tools()
chrome.change_url("www.google.com")


for i in xrange(4):
    type(Key.DOWN, KeyModifier.CMD)
    wait("1379702587714.png")

    type(str(i+1))
    type(Key.ESC)

    if i == 3:
        chrome.open_developer_tools_vertical()
        chrome.close_developer_tools()