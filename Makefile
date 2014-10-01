################################################################################
#
#   Makefile for RMG Py
#
################################################################################

.PHONY : all minimal main measure solver cantherm clean decython documentation QM

all: main measure solver QM
	
noQM: main measure solver

minimal:
	python setup.py build_ext minimal --build-lib . --build-temp build --pyrex-c-in-temp

main:
	echo "Checking you have PyDQED..."
	@ python -c 'import pydqed; print pydqed.__file__'
	python setup.py build_ext main --build-lib . --build-temp build --pyrex-c-in-temp

measure:
	python setup.py build_ext measure --build-lib . --build-temp build --pyrex-c-in-temp

solver:
	echo "Checking you have PyDAS..."
	@ python -c 'import pydas; print pydas.__file__'
	python setup.py build_ext solver --build-lib . --build-temp build --pyrex-c-in-temp

cantherm:
	python setup.py build_ext cantherm --build-lib . --build-temp build --pyrex-c-in-temp

bin/symmetry:
	$(MAKE) -C external/symmetry install

QM: bin/symmetry
	echo "Checking you have rdkit..."
	@ python -c 'import rdkit; print rdkit.__file__'
	echo "Checking rdkit has InChI support..."
	@ python -c 'from rdkit import Chem; assert Chem.inchi.INCHI_AVAILABLE, "RDKit installed without InChI Support"'

documentation:
	$(MAKE) -C documentation html
	echo "Start at: documentation/build/html/index.html"

clean:
	python setup.py clean --build-temp build
	rm -rf build/
	find . -name '*.so' -exec rm -f '{}' \;
	find . -name '*.pyc' -exec rm -f '{}' \;
	$(MAKE) -C external/symmetry clean
	rm -f bin/symmetry

decython:
	# de-cythonize all but the 'minimal'. Helpful for debugging in "pure python" mode.
	find . -name *.so ! \( -name _statmech.so -o -name quantity.so -o -regex '.*rmgpy/measure/.*' -o -regex '.*rmgpy/solver/.*' \) -exec rm -f '{}' \;
	find . -name *.pyc -exec rm -f '{}' \;

test:
	mkdir -p testing/coverage
	rm -rf testing/coverage/*
	nosetests --nocapture --nologcapture --all-modules --verbose --with-coverage --cover-inclusive --cover-package=rmgpy --cover-erase --cover-html --cover-html-dir=testing/coverage rmgpy

eg1: noQM
	mkdir -p testing/minimal
	rm -rf testing/minimal/*
	cp examples/rmg/minimal/input.py testing/minimal/input.py
	coverage erase
	echo "Running minimal example with coverage tracking AND profiling"
	coverage run rmg.py -p testing/minimal/input.py
	coverage report
	coverage html
eg2: all
	mkdir -p testing/hexadiene
	rm -rf testing/hexadiene/*
	cp examples/rmg/1,3-hexadiene/input.py testing/hexadiene/input.py
	coverage erase
	echo "Running 1,3-hexadiene example with coverage tracking AND profiling"
	coverage run rmg.py -p testing/hexadiene/input.py
	coverage report
	coverage html
eg3: all
	mkdir -p testing/liquid_phase
	rm -rf testing/liquid_phase/*
	cp examples/rmg/liquid_phase/input.py testing/liquid_phase/input.py
	coverage erase
	echo "Running liquid_phase example with coverage tracking AND profiling"
	coverage run rmg.py -p testing/liquid_phase/input.py
	coverage report
	coverage html
