from BrowserPackage.StartBrowser import open_browser
from BrowserPackage.StopBrowser import close_browser


class TestCase:
    def test_Case(self):
        open_browser()
        print("Hello Running TC")
        close_browser()


obj_tc = TestCase()
obj_tc.test_Case()




