
tests-watch:
	ptw -- --cov-report term:skip-covered --cov=app --cov-config=.coveragerc tests

tests-report:
	pytest --cov=app --cov-report html:cov_html tests