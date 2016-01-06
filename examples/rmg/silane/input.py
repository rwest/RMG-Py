# Data sources
database(
    thermoLibraries = ['SiliconHydrideLibrary', 'primaryThermoLibrary'],
    reactionLibraries = [('Silicon_Giunta_1990', False), ('DolletSi2H4', False)],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['R_Recombination', 'Silylene_Insertion', 'Silylene_to_Silene', 'H_Abstraction', 'H2_transfer'],
    kineticsEstimator = 'rate rules',
)

# List of species
species(
    label='SiH4',
    reactive=True,
    structure=SMILES("[SiH4]")
)

species(
    label='Ar',
    reactive=False,
    structure=SMILES("[Ar]")
)

# Reaction systems
simpleReactor(
    temperature=(913,'K'),
    pressure=(39000,'Pa'),
    initialMoleFractions={
        "SiH4": 0.00016,
	"Ar": 0.99984,
    },
    terminationConversion={
        'SiH4': 0.9,
    },
    terminationTime=(1, 's')
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.1,
    toleranceInterruptSimulation=0.5,
    maximumEdgeSpecies=100000
)

#pressureDependence(
#    method='modified strong collision',
#    maximumGrainSize=(0.5,'kcal/mol'),
#    minimumNumberOfGrains=250,
#    temperatures=(300,2000,'K',8),
#    pressures=(0.01,20,'bar',5),
#    interpolation=('Chebyshev', 6, 4),
#)

options(
    units='si',
    saveRestartPeriod=None,
    drawMolecules=True,
    generatePlots=False,
    saveEdgeSpecies=True,
)

generatedSpeciesConstraints(
    maximumSiliconAtoms=6
)


