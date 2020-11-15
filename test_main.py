import unittest
import numpy as np
from main import *

class UnitTests(unittest.TestCase) :
    def test_energy(self) : 
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
              spins[j] = np.floor( num / 2**(4-j) )
              num = num - spins[j]*2**(4-j)
              if spins[j]==0 : spins[j] = -1
            sumspins = sum( spins )
            meanspin = sumspins / len(spins)
            self.assertTrue( np.abs( hamiltonian( spins, 1, 2)+(1+4*meanspin)*sumspins )<1e-7 )
            self.assertTrue( np.abs( hamiltonian( spins, -1, 3)+(-1+6*meanspin)*sumspins )<1e-7 )
            self.assertTrue( np.abs( hamiltonian( spins, 0, 3)+(6*meanspin)*sumspins )<1e-7 )
            self.assertTrue( np.abs( hamiltonian( spins, 2, 2)+(2+4*meanspin)*sumspins )<1e-7 )
