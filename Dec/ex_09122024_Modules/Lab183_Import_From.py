from BrowserPackage.StartBrowser import open_browser
from BrowserPackage.StopBrowser import close_browser

def test_Case():
    open_browser()
    print("Hello Running TC")
    close_browser()

test_Case()