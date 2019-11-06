#!/usr/bin/env python
# coding: utf-8

# # Generate Low Temperature Reactions
# 
# The goal of this notebook is to allow you to generate all the species that would occur by systematically applying known low-temperature pathways to a starting fuel molecule.
# 
# You might do this to generate species that you then put into an RMG input file.
# 
# It is based on a similar notebook for generating reactions. 
# 
# This script performs the same task as the script in `scripts/generateReactions.py` but in visual ipynb format.
# It can also evaluate the reaction forward and reverse rates at a user selected temperature.

# In[1]:


import sys, os
sys.path.insert(0,os.path.expandvars("$RMGpy"))


# In[2]:


from rmgpy.rmg.main import RMG
from rmgpy.rmg.model import CoreEdgeReactionModel
from rmgpy import settings
from IPython.display import display
from arkane.output import prettify


# Declare database variables here by changing the thermo and reaction libraries, or restrict to certain reaction families.  

# In[3]:


database = """
database(
    thermoLibraries = ['BurkeH2O2','primaryThermoLibrary','DFT_QCI_thermo','CBS_QB3_1dHR','Narayanaswamy','Chernov'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = [
    'H_Abstraction',
    'R_Recombination',
    'R_Addition_MultipleBond',
    'intra_H_migration',
    'Intra_R_Add_Endocyclic',
    'Intra_R_Add_Exocyclic'
    ],
    kineticsEstimator = 'rate rules',
)

options(
    verboseComments=True,  # Set to True for detailed kinetics comments
)
"""


# List all species you want reactions between

# In[4]:


speciesList = """
species(
    label='c10',
    reactive=True,
    structure=SMILES("CCCCCCCCCC")
)

species(
    label='o2',
    reactive=True,
    structure=SMILES("[O][O]")
)
"""


# In[5]:


# Write input file to disk
os.makedirs('temp',exist_ok=True)
inputFile = open('temp/input.py','w')
inputFile.write(database)
inputFile.write(speciesList)
inputFile.close()


# In[6]:


# initialize RMG instance
from rmgpy.tools.generate_reactions import RMG
kwargs = {
            'restart': '',
            'walltime': '00:00:00:00',
            'kineticsdatastore': True
    }
rmg = RMG(input_file='temp/input.py', output_directory='temp')

rmg.initialize(**kwargs)


# In[44]:


from rmgpy.molecule import Molecule
m = Molecule(smiles='CCCCCCCCCC')
h = Molecule(smiles='[H]')
reactions = rmg.database.kinetics.react_molecules(, only_families='H_Abstraction')
for r in reactions:
    r.products


# In[53]:


molecules = defaultdict(set)
molecules['fuel'].add(Molecule(smiles='CCCCCCCCCC'))
molecules['H'].add(Molecule(smiles='[H]'))
molecules


# In[61]:


def union(*args):
    out = set()
    for a in args:
        out.update(molecules[a])
    return out


# In[63]:


union('fuel','H')


# In[72]:


# React fuel with H to get the radicals R
reactions = rmg.database.kinetics.react_molecules(union('fuel', 'H'), only_families='H_Abstraction')
for r in reactions:
    for prod in r.products:
        if prod.get_formula() == 'H2':
            continue
        molecules['R'].add(prod)
molecules


# In[73]:


molecules['O2'].add(Molecule(smiles='[O][O]'))
molecules


# In[91]:


# React R with O2 to get the ROO
o2 = list(molecules['O2'])[0]
for s in molecules['R']:
    reactions = rmg.database.kinetics.generate_reactions_from_families((s, o2), only_families='R_Recombination')
    display(s)
    for r in reactions:
        print(r)
        molecules['ROO'].add(r.products[0].molecule[0])
molecules


# In[92]:


# Isomerize ROO to get QOOH
for s in molecules['ROO']:
    reactions = rmg.database.kinetics.generate_reactions_from_families((s, ), only_families='intra_H_migration')
    display(s)
    for r in reactions:
        print(r)
        molecules['QOOH'].add(r.products[0].molecule[0])
molecules


# In[93]:


# React QOOH with O2 to get the O2QOOH
o2 = list(molecules['O2'])[0]
for s in molecules['QOOH']:
    reactions = rmg.database.kinetics.generate_reactions_from_families((s, o2), only_families='R_Recombination')
    display(s)
    for r in reactions:
        print(r)
        molecules['OOQOOH'].add(r.products[0].molecule[0])
molecules


# In[95]:


print("These are the OOQOOH")
for m in molecules['OOQOOH']:
    display(m)


# In[96]:


# What next? OH + keto-hydroperoxide or HO2 + alkenyl hydroperoxide 


# In[ ]:





# In[ ]:




