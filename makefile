make dummy_data:
	python3 -m utility.dummy_data

make flask run:
	flask run

make docker build:
	docker build -t money_mover .

make docker run:
	docker run -d --name money_mover -p 5000:5000 money_mover

