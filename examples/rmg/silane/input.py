# Data sources
database(
    thermoLibraries = ['primaryThermoLibrary'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['H_Abstraction', 'Silylene_Insertion'],
    kineticsEstimator = 'rate rules',
)

# List of species
species(
    label='SiH4',
    reactive=True,
    structure=SMILES("[SiH4]")
)

species(
    label='H2',
    reactive=True,
    structure=SMILES("[H][H]")
)

# Reaction systems
simpleReactor(
    temperature=(800,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "SiH4": 0.9,
	"H2": 0.1
    },
    terminationConversion={
        'SiH4': 0.9,
    },
    terminationTime=(1e6,'s'),
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.1,
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=100000
)

options(
    units='si',
    saveRestartPeriod=None,
    drawMolecules=False,
    generatePlots=False,
    saveEdgeSpecies=True,
    saveConcentrationProfiles=True,
)
