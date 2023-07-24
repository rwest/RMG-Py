# Coordinates for Toluene in Input Orientation (angstroms):
#   C    0.0083    0.7200    0.0000
#   C    0.0111    0.0014    1.2001
#   C    0.0111   -1.3915    1.2030
#   C    0.0102   -2.0941    0.0000
#   C    0.0111   -1.3915   -1.2030
#   C    0.0111    0.0014   -1.2001
#   C   -0.0240    2.2298    0.0000
#   H    0.0157    0.5394    2.1431
#   H    0.0157   -1.9280    2.1456
#   H    0.0132   -3.1783    0.0000
#   H    0.0157   -1.9280   -2.1456
#   H    0.0157    0.5394   -2.1431
#   H   -1.0549    2.6011    0.0000
#   H    0.4700    2.6394    0.8842
#   H    0.4700    2.6394   -0.8842
conformer(
    label = 'Toluene',
    E0 = (30.8379, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(92.0626, 'amu')),
        NonlinearRotor(
            inertia = ([90.9803, 200.823, 288.663], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([86.0672, 344.741, 416.416, 422.781, 531.041, 640.189, 651.576, 717.784, 802.109, 807.92, 857.364, 934.232, 979.01, 1003.84, 1004.11, 1022.2, 1055.84, 1115.62, 1185.71, 1207.89, 1233.8, 1333.07, 1361.39, 1375.83, 1426.73, 1476.17, 1510.12, 1535.9, 1633.21, 1655.24, 2618.2, 3038.2, 3113.31, 3164.24, 3165.86, 3178.51, 3186.97, 3199.77], 'cm^-1'),
        ),
        FreeRotor(inertia=(7.33475, 'amu*angstrom^2'), symmetry=6),
    ],
    spin_multiplicity = 1,
    optical_isomers = 1,
)

# Thermodynamics for Toluene:
#   Enthalpy of formation (298 K)   =    11.826 kcal/mol
#   Entropy of formation (298 K)    =    79.274 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      25.503      11.877      79.444     -11.957
#            400      33.462      14.831      87.888     -20.325
#            500      40.423      18.535      96.125     -29.527
#            600      46.272      22.878     104.026     -39.538
#            800      55.538      33.108     118.677     -61.834
#           1000      62.224      44.921     131.830     -86.909
#           1500      71.652      78.721     159.111    -159.945
#           2000      76.112     115.767     180.395    -245.023
#           2400      78.576     146.724     194.499    -320.073
#    =========== =========== =========== =========== ===========
thermo(
    label = 'Toluene',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.98801, -0.000176824, 0.000171986, -2.90618e-07, 1.56368e-10, 3752.67, 11.8438],
                Tmin = (10, 'K'),
                Tmax = (560.884, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.50591, 0.062379, -3.87519e-05, 1.14998e-08, -1.30888e-12, 4225.63, 37.1404],
                Tmin = (560.884, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (31.1792, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (353.365, 'J/(mol*K)'),
    ),
)

