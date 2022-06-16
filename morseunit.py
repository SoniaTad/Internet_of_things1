import unittest
import morse
class TestMorse(unittest.TestCase):
    def test_encode_us(self):
        self.assertEqual( morse.encode('us'), '..- ... ')
        self.assertEqual( morse.encode('u'), '..- ')
        self.assertEqual( morse.encode('hello world'), '.... . .-.. .-.. ---  .-- --- .-. .-.. -.. ')
        self.assertEqual( morse.encode(''), 'nothing to encode')
        #this next test is designed to fail as the encode function is supposed to return 'nothing to encode' 
        #self.assertEqual( morse.encode(''), '')
        self.assertEqual( morse.encode('£'), ' ')
        self.assertEqual( morse.encode('12'), '.---- ..--- ')
        
        #testing the decode function 
        self.assertEqual(morse.decode('..- ...'), 'US')
        self.assertEqual(morse.decode('..-'), 'U')
        self.assertEqual(morse.decode('.  .'), 'E*E')
        self.assertEqual(morse.decode('.... . .-.. .-.. ---  .-- --- .-. .-.. -..'), 'HELLO*WORLD')
        #this test is supposed to fail because of the lowercase decode returns the msg in uppercase 
        #running this next line will lead to an error message 
        #self.assertEqual(morse.decode('.... . .-.. .-.. ---  .-- --- .-. .-.. -..'), 'hello*world')
        self.assertEqual(morse.decode(''), '*')
        self.assertEqual(morse.decode('..........'), 'error')
        self.assertEqual(morse.decode('.....'), '5')

        #Task 4 testing :
        self.assertEqual( morse.encode('$'), '...-..- ')
        self.assertEqual( morse.encode('( :'), '-.--.  ---... ')
        self.assertEqual( morse.encode(',.'), '--..-- .-.-.- ')
        self.assertEqual(morse.decode('...-..- .-.-.- --..-- -..-. -.--. -.--.-'), '$.,/()')
        self.assertEqual(morse.decode('...-..-  .-.-.- --..-- -..-.  -.--. -.--.-'), '$*.,/*()')
        self.assertEqual(morse.decode('..--- ----- ...-..-'), '20$')
if __name__ == '__main__':
    unittest.main()