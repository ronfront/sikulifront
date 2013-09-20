# NOTE ENSURE DEVELOPER TOOLS ON AND ITS TO MINIMUM SIZE!
# functions

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