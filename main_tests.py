import unittest

from tests.tests_1d import Test1D
from tests.tests_3d import Test3D
from tests.tests_temporal_layout import TestTL
from tests.tests_histo import TestHisto


def create_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()    
    suite.addTests(loader.loadTestsFromTestCase(Test1D))
    suite.addTests(loader.loadTestsFromTestCase(Test3D))
    suite.addTests(loader.loadTestsFromTestCase(TestTL))
    suite.addTests(loader.loadTestsFromTestCase(TestHisto))

    return suite

# 4. Run the Suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2) # Use verbosity=2 for detailed output
    test_suite = create_suite()
    result = runner.run(test_suite)
    
    print(f"\nTests Run: {result.testsRun}")
    print(f"Errors: {len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
