import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        # 用於測試結果是不是我們所預期的
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        # 用於測試 True or False 的狀態
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # 用於測試某個特定的例外有無發生
        with self.assertRaises(TypeError):  
            s.split(2)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_upper'))
    suite.addTest(TestStringMethods('test_isupper'))
    return suite

if __name__ == '__main__':
    # unittest.main()
    unittest.TextTestRunner().run(suite())