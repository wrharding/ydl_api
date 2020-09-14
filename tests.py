import main
import unittest

class Tests(unittest.TestCase):

    #Tests with no_playlist = True
    def test_must_be_checked_no_playlist(self):
        self.assertTrue(main.must_be_checked("https://www.youtube.com/playlist?list=PL8Zccvo5Xlj53ESRIn2Q4lg2DvKIB92sj", True) is False) #playlist only
        self.assertTrue(main.must_be_checked("https://www.youtube.com/watch?v=Ax4uSTdkp04", True) is True) #video only
        self.assertTrue(main.must_be_checked("https://www.youtube.com/watch?v=Ax4uSTdkp04&list=PL8Zccvo5Xlj53ESRIn2Q4lg2DvKIB92sj&index=10&t=0s", True) is True) #video in playlist
        self.assertTrue(main.must_be_checked("https://twitter.com/Totonyus/status/1198152820232314885", True) is True) #not youtube

    #Tests with no_playlist = False
    def test_must_be_checked_with_playlist(self):
        self.assertTrue(main.must_be_checked("https://www.youtube.com/playlist?list=PL8Zccvo5Xlj53ESRIn2Q4lg2DvKIB92sj", False) is False) #playlist only
        self.assertTrue(main.must_be_checked("https://www.youtube.com/watch?v=Ax4uSTdkp04", False) is True) #video only
        self.assertTrue(main.must_be_checked("https://www.youtube.com/watch?v=Ax4uSTdkp04&list=PL8Zccvo5Xlj53ESRIn2Q4lg2DvKIB92sj&index=10&t=0s", False) is False) #video in playlist
        self.assertTrue(main.must_be_checked("https://twitter.com/Totonyus/status/1198152820232314885", False) is True) #not youtube

    def test_check_download(self):
        self.assertTrue(main.check_download("https://www.youtube.com/watch?v=Ax4uSTdkp04", 'best')['errors'] is False)
        self.assertTrue(main.check_download("https://www.youtube.com/watch?v=Ax4uSTdkp04", 'b3st')['errors'] is True)
        self.assertTrue(main.check_download("https://www.youtube.com/playlist?list=PL8Zccvo5Xlj53ESRIn2Q4lg2DvKIB92sj", 'b3st')['checked'] is False)

if __name__ == '__main__':
    unittest.main()
