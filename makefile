test-full:
	pytest && ./node_modules/.bin/cypress run

cypress-open:
	./node_modules/.bin/cypress open

cypress:
	./node_modules/.bin/cypress
