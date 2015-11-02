#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
#from external.wip import work_in_progress

from rmgpy import settings
from rmgpy.species import Species
from rmgpy.data.thermo import ThermoDatabase
from rmgpy.molecule.molecule import Molecule

################################################################################

class TestThermoDatabase(unittest.TestCase):
    """
    Contains unit tests of the ThermoDatabase class.
    """
    # Only load these once to save time
    database = ThermoDatabase()
    database.load(os.path.join(settings['database.directory'], 'thermo'))


    def setUp(self):
        
        self.database = self.__class__.database

        self.Tlist = [300, 400, 500, 600, 800, 1000, 1500]
        
        self.testCases = [
            # SMILES            symm  H298     S298     Cp300  Cp400  Cp500  Cp600  Cp800  Cp1000 Cp1500
            ['ClCC(Cl)(Cl)C(Cl)Cl',  1,  -26.05, 93.5, 28.04, 31.86, 34.85, 37, 40, 42, 45]
            #['ClC[C](Cl)C(Cl)(Cl)Cl',   3,    -8.758, 105.970, 32.83, 36.98, 40.2, 42.74, 46.3, 48, 51],
  			#['ClCC(Cl)=C(Cl)Cl',  1,  -26.05, 93.5, 28.04, 31.86, 34.85, 37, 40, 42, 45]

        ]
      
    def testChlorineThermoGeneration(self):
        """
        Test the thermo for the chlorinated species from GA
        """
        
        for smiles, symm, H298, S298, Cp300, Cp400, Cp500, Cp600, Cp800, Cp1000, Cp1500 in self.testCases:
            Cplist = [Cp300, Cp400, Cp500, Cp600, Cp800, Cp1000, Cp1500]

            print smiles
            print Cplist
            species = Species(molecule=[Molecule(SMILES=smiles)])
            species.generateResonanceIsomers()
            species.molecule[0]
            molecule = species.molecule[0]
            print molecule
            
            thermoData = self.database.getThermoDataFromGroups(species)
            print thermoData
            #thermoDataa = self.database.estimateThermoViaGroupAdditivityForSaturatedStructWithoutSymmetryCorrection(molecule)
            #print thermoDataa
            #tdata = self.database.estimateThermoViaGroupAdditivity(molecule)
            #print tdata
            tdata = self.database.estimateRadicalThermoViaHBI(species.molecule[0], self.database.estimateThermoViaGroupAdditivity)
            print tdata



            if smiles is 'ClC[C](Cl)C(Cl)(Cl)Cl': import ipdb; ipdb.set_trace()
            self.assertAlmostEqual(H298, tdata.getEnthalpy(298) / 4184, places=1, msg="H298 error for {0}: {1} vs {2}".format(smiles, H298, tdata.getEnthalpy(298)/4184))
            self.assertAlmostEqual(S298, tdata.getEntropy(298) / 4.184, places=1, msg="S298 error for {0}: {1} vs {2}".format(smiles, S298, tdata.getEntropy(298)/4.184))
            self.assertAlmostEqual(Cp500, tdata.getHeatCapacity(500) / 4.184, places=1, msg="Cp500 error for {0}".format(smiles))
            
################################################################################

if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2))

