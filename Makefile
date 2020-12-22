run:
	docker-compose up --build

clear:
	docker-compose down

tests:
	docker-compose -f docker-compose.test.yml -p tests up --build --abort-on-container-exit
