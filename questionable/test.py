from main import qq
import unittest

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(qq(5,0),5)
		self.assertEqual(qq(0,5),5)
		self.assertEqual(qq(5,10),5)
		self.assertEqual(qq(10,5),10)
		self.assertEqual(qq(0,0),None)

		self.assertEqual(qq(5.0,0.0),5.0)
		self.assertEqual(qq(0.0,5.0),5.0)
		self.assertEqual(qq(5.0,10.0),5.0)
		self.assertEqual(qq(10.0,5.0),10.0)
		self.assertEqual(qq(0.0,0.0),None)

		self.assertEqual(qq("cat",""),"cat")
		self.assertEqual(qq("","dog"),"dog")
		self.assertEqual(qq("cat","dog"),"cat")
		self.assertEqual(qq("dog","cat"),"dog")
		self.assertEqual(qq("",""),None)

		self.assertEqual(qq("cat",None),"cat")
		self.assertEqual(qq(None,"dog"),"dog")
		self.assertEqual(qq(None,None),None)

		self.assertEqual(qq([1,2,3,4],[]),[1,2,3,4])
		self.assertEqual(qq([],[1,2,3,4]),[1,2,3,4])
		self.assertEqual(qq([1,2,3,4],[5,6,7,8]),[1,2,3,4])
		self.assertEqual(qq([],[]),None)

		self.assertEqual(qq((1,2,3,4),()),(1,2,3,4))
		self.assertEqual(qq((),(1,2,3,4)),(1,2,3,4))
		self.assertEqual(qq((1,2,3,4),(5,6,7,8)),(1,2,3,4))
		self.assertEqual(qq((),()),None)

		self.assertEqual(qq({1,2,3,4},{}),{1,2,3,4})
		self.assertEqual(qq({},{1,2,3,4}),{1,2,3,4})
		self.assertEqual(qq({1,2,3,4},{5,6,7,8}),{1,2,3,4})
		self.assertEqual(qq({},{}),None)

if __name__ == '__main__':
	unittest.main()