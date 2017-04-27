import unittest
import numpy as np

class TestPB1(unittest.TestCase):
    '''
    Problem 1 from Liao and Shoemaker
    '''

    def test_to_EclipJ2000(self):
        expectations = [
            [-148030923.95108017, -12123548.951590259, 302492.17670564854, 2.6590243298160754, -29.849194304414752, -0.35374685933315347],
            [-134976740.1465185, -64019984.225526303, 173268.29557571266, 12.914400364190689, -26.830454218461472, -0.48247193678732703],
            [-91834879.055177972, -119989870.393112, 265756.61887669913, 23.896559117820097, -18.302614365094886, -0.39983700293859631],
            [146717590.82034796, 24671383.129385762, -52708.613323677433, -6.003251556028836, 28.634454862602379, -0.09470460569670297],
        ]
        for tno, epoch in enumerate(self.epochs):
            st = ChgFrame(self.state, 'IAU_Earth', 'EclipJ2000', epoch)
            for i, component in enumerate(st):
                eps = self.epsDecimalsR if i < 3 else self.epsDecimalsV
                self.assertAlmostEqual(component, expectations[tno][i], eps, '{} {}[{}]'.format(epoch, 'R' if i < 3 else 'V', i))
            # Check reversiblity
            revst = ChgFrame(st, 'EclipJ2000', 'IAU_Earth', epoch)
            for i, component in enumerate(revst):
                eps = self.epsDecimalsR if i < 3 else self.epsDecimalsV
                self.assertAlmostEqual(component, self.state[i], eps, '{} {}'.format(epoch, 'R (rev\'d)' if i < 3 else 'V (rev\'d)'))

if __name__ == '__main__':
    unittest.main()
