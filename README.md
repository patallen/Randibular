# Randibular
Pytest usage / features demonstration

### Setup
1. Create virtualenv
2. activate the virtualenv `source <virtualenv>/bin/activate`
3. `pip install -r requirements.txt`


### Running Tests
1. All tests in 'test_*' files:
    - `pytest`
2. Include doctests:
    - `pytest --doctest-modules`
3. Run a test with a specific 'mark':
    - `pytest -m <mark-name>`


### Useful things
1. `pytest --fixtures` - list all available fixtures & descriptions
2. `pytest --last-failed` - only run tests that failed on the last pass
