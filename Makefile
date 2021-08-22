.PHONY: mypy pycodestyle pylint pytest

clean-doc:
	cd docs && make clean

doc:
	cd docs && make html

mypy:
	mypy --show-error-codes src/ 

pycodestyle:
	pycodestyle src/ tests/ 

pylint:
	PYTHONPATH=src/ pylint -rn src/ tests/ 

pytest:
	PYTHONPATH=src/ pytest -v -s tests/
