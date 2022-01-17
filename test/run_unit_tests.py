import unittest


# Run all unit tests
unittests = unittest.TestLoader().discover('.', pattern='unittest_*.py')

runner = unittest.TextTestRunner()
runner.run(unittests)
