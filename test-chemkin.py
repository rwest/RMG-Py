#%% 
import os
from rmgpy.reaction import Reaction
from rmgpy.molecule import Molecule
from rmgpy.species import Species
from rmgpy.chemkin import loadChemkinFile
from rmgpy.exceptions import ChemkinError, AtomTypeError
import re
import importChemkin
from importChemkin import ModelMatcher
#%% 
reload(importChemkin)
from importChemkin import ModelMatcher

#%% 
modelspath = os.path.expanduser("../RMG-models")
generator = os.walk(modelspath)
chemkin_file = None
thermo_file = None

models = {}

class Args(object):
    pass

for path, sub_dirs, files in generator:

    if "import.sh" in files:
        model = path.replace(modelspath, "")
        print "Attempting to read in {}".format(model)
        f = open(os.path.join(path, "import.sh"))

        script = f.read()
        species = re.search('--species +(\S+)', script).group(1)
        reactions = re.search('--reactions +(\S+)', script).group(1)
        thermo = re.search('--thermo +(\S+)', script).group(1)
        known = re.search('--known +(\S+)', script).group(1)
        
        args = Args()
        args.__dict__.update({
                'species': os.path.join(path,species or thermo),
                'reactions': os.path.join(path,reactions or thermo),
                'thermo': os.path.join(path,thermo),
                'known': os.path.join(path,known or 'SMILES.txt'),
                'minimal': True,})

        mm = ModelMatcher(args)
        mm.minimal()

        print '-'*80
        continue


#%%
