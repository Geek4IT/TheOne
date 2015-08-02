import unittest
import tornado.testing

TEST_MODULES = [
	
]

def all():
	try:
		return unittest.defaultTestLoader.loadTestsFromNames(TEST_MODULE)
	except AttributeError as e:
		if "'module' object has no attribute 'test_" in str(e):
			for m in TEST_MODULES:
				__import__(m, globals(), locals())
		raise

if __name__ == '__main__':
	tornado.testing.main()
