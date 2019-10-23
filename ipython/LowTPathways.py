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

# In[2]:


import sys, os
sys.path.insert(0,os.path.expandvars("$RMGpy"))


# In[3]:


from rmgpy.rmg.main import RMG
from rmgpy.rmg.model import CoreEdgeReactionModel
from rmgpy import settings
from IPython.display import display
from arkane.output import prettify


# Declare database variables here by changing the thermo and reaction libraries, or restrict to certain reaction families.  

# In[5]:


database = """
database(
    thermoLibraries = ['BurkeH2O2','primaryThermoLibrary','DFT_QCI_thermo','CBS_QB3_1dHR','Narayanaswamy','Chernov'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = [
    'H_Abstraction',
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

# In[26]:


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


# In[27]:


# Write input file to disk
os.makedirs('temp',exist_ok=True)
inputFile = open('temp/input.py','w')
inputFile.write(database)
inputFile.write(speciesList)
inputFile.close()


# In[25]:


# initialize RMG instance
from rmgpy.tools.generate_reactions import RMG
kwargs = {
            'restart': '',
            'walltime': '00:00:00:00',
            'kineticsdatastore': True
    }
rmg = RMG(input_file='temp/input.py', output_directory='temp')

rmg.initialize(**kwargs)


# In[34]:


for n, s in rmg.reaction_model.species_dict.items():
    print(n)
    display(s[0])


# In[38]:


rmg.bimolecular_react


# In[17]:




rmg.reaction_model.enlarge(react_edge=True,
                           unimolecular_react=rmg.unimolecular_react,
                           bimolecular_react=rmg.bimolecular_react,
                           trimolecular_react=rmg.trimolecular_react)
# Show all core and edge species and reactions in the output
rmg.reaction_model.output_species_list.extend(rmg.reaction_model.edge.species)
rmg.reaction_model.output_reaction_list.extend(rmg.reaction_model.edge.reactions)

rmg.save_everything()

rmg.finish()


# In[20]:


get_ipython().run_line_magic('pinfo', 'RMG')


# In[13]:


rmg.reaction_model.output_reaction_list


# In[6]:


# Pick some temperature to evaluate the forward and reverse kinetics
T = 623.0 # K


# In[7]:


for rxn in rmg.reactionModel.outputReactionList:
    print '========================='
    display(rxn)
    print 'Reaction Family = {0}'.format(rxn.family)
    print ''
    print 'Reactants'
    for reactant in rxn.reactants:
        print 'Label: {0}'.format(reactant.label)
        print 'SMILES: {0}'.format(reactant.molecule[0].toSMILES())
        print ''
    print 'Products'
    for product in rxn.products:
        print 'Label: {0}'.format(product.label)
        print 'SMILES: {0}'.format(product.molecule[0].toSMILES())
    print ''
    print rxn.toChemkin()
    print ''
    print 'Heat of Reaction = {0:.2F} kcal/mol'.format(rxn.getEnthalpyOfReaction(623.0)/4184)
    print 'Forward kinetics at {0} K: {1:.2E}'.format(T, rxn.getRateCoefficient(T))

    reverseRate = rxn.generateReverseRateCoefficient()
    print 'Reverse kinetics at {0} K: {1:.2E}'.format(T, reverseRate.getRateCoefficient(T))


# In[ ]:




