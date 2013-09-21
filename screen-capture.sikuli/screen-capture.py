# NOTE ENSURE DEVELOPER TOOLS ON AND ITS TO MINIMUM SIZE!
# functions

# force quit = CMD + SHIFT + C


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
        self.wait_page_load()
        
    def wait_page_load(self):
        if exists("1379707599945.png"):
            waitVanish("1379707599945.png")
        wait("1379707510263.png")

#  ----------------------------------

def awesome_screenshot(saveName, mode="full"):
    # use a key based approach
    saveName = saveName + "_" + mode

    ### hotkey for awesome screenshot (preset as CMD+Up Arrow)
    type(Key.UP, KeyModifier.CMD)
    wait("1379709490639.png")
    if mode == "full":
        click("1379709478440.png")
    elif mode == "screen":
        click("1379730411669.png")

    # switch to annotate screens 
    wait(Pattern("1379721262671.png").exact(), 30)
    chrome.active_regular()

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

#  ----------------------------------

user_agent_switch = False
chrome = Chrome()
platforms_to_fetch = ["desktop", "tabletl", "tabletp", "iphonep"]

sites = [
    ["storefront-staging.herokuapp.com/", "home", "v0"],
    ["storefront-staging.herokuapp.com/about", "about", "v0"],
    ["storefront-staging.herokuapp.com/how-it-works", "how-it-works", "v0"],
    ["storefront-staging.herokuapp.com/contact", "contact", "v0"],
    ["storefront-staging.herokuapp.com/press", "press", "v0"],
    ["storefront-staging.herokuapp.com/team", "team", "v0"],
    ["storefront-staging.herokuapp.com/properties?address=San%20Francisco,%20CA#/sortField=price&minPrice=0&maxPrice=125000.0&minSize=0&maxSize=50000&mapLat=37.773187224778546&mapLng=-122.41041460000002&priceTypeDay=true&priceTypeWeek=true&priceTypeMonth=true&page=1", "properties", "v0"],
    ["storefront-staging.herokuapp.com/properties/3927-24th-st-san-francisco-ca-94114-usa", "properties-show", "v0"],
        
    ["localhost:3000/", "home", "v1"],
    ["localhost:3000/about", "about", "v1"],
    ["localhost:3000/how-it-works", "how-it-works", "v1"],
    ["localhost:3000/contact", "contact", "v1"],
    ["localhost:3000/press", "press", "v1"],
    ["localhost:3000/team", "team", "v1"],
    ["localhost:3000/properties?address=San%20Francisco,%20CA#/sortField=price&minPrice=0&maxPrice=125000.0&minSize=0&maxSize=50000&mapLat=37.773187224778546&mapLng=-122.41041460000002&priceTypeDay=true&priceTypeWeek=true&priceTypeMonth=true&page=1", "properties", "v1"],
    ["localhost:3000/properties/3927-24th-st-san-francisco-ca-94114-usa", "properties-show", "v1"],
    ]
        
resizers = [
    ["1379708197381.png", "desktop", "1379714057828.png", "1379714175863.png"], 
    ["1379708584510.png", "tabletl", "1379714078771.png", "1379714208816.png"],
    ["1379708595257.png", "tabletp", "1379714078771.png", "1379714208816.png"],
    ["1379708612919.png", "iphonep", "1379714078771.png", "1379714221797.png"]]

#  ----------------------------------

for resize, platform, ua_menu, ua_sub in resizers:
    if platform not in platforms_to_fetch:
        continue
    
    chrome.active_incognito()
    chrome.close_developer_tools()
    
    ### hotkey for user agent switcher
    if user_agent_switch:
        type(Key.RIGHT, KeyModifier.CMD)
        click(ua_menu)
        wait(ua_sub)
        click(ua_sub)
        chrome.wait_page_load()

    ### hotkey for window resizer
    type(Key.DOWN, KeyModifier.CMD)
    wait("1379716504266.png")
    click(resize)

    # note iPhone requires a google vertical developer
    if resize == "1379708612919.png":
        waitVanish("1379716504266.png")
        chrome.open_developer_tools(orientation="vertical")
        click("1379707470322.png")

    #  ----------------------------------

    for url, handle, version in sites:
        chrome.change_url(url)
        saveName = "_".join([handle, platform, version])
        awesome_screenshot(saveName, "full")
        awesome_screenshot(saveName, "screen")
 