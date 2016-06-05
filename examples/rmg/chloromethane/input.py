# coding: utf-8

database(
    thermoLibraries = ['primaryThermoLibrary'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = 'default',
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)

species(
    label = "CH3Cl",
    reactive = True,
    structure = adjacencyList(
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 Cl u0 p3 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
"""),
)

species(
    label = "oxygen",
    reactive = True,
    structure = adjacencyList(
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
"""),
)

species(
    label = "Argon",
    reactive = False,
    structure = adjacencyList(
"""
1 Ar u0 p4 c0
"""),
)

simpleReactor(
    temperature = (2500,"K"),
    pressure = (1.01,"bar"),
    initialMoleFractions={
        "CH3Cl": 0.1,
        "Argon": 0.75,
        "oxygen": 0.15,
    },
    terminationTime = (1,"s"),
    terminationConversion = { 'CH3Cl': 0.99 },
)

simulator(
    atol = 1e-16,
    rtol = 1e-08,
    sens_atol = 1e-06,
    sens_rtol = 0.0001,
)

model(
    toleranceMoveToCore = 0.1,
    toleranceKeepInEdge = 0,
    toleranceInterruptSimulation = 1,
    maximumEdgeSpecies = 100000,
    minCoreSizeForPrune = 50,
    minSpeciesExistIterationsForPrune = 2,
    filterReactions = 0,
)

options(
    units = "si",
    saveRestartPeriod = None,
    generateOutputHTML = True,
    generatePlots = False,
    saveSimulationProfiles = False,
    saveEdgeSpecies = False,
    verboseComments = False,
)


