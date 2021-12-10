dummy_data:
	python3 -m webapp.utility.dummy_data

flask run:
	flask run

docker build:
	docker build -t money_mover .

docker run:
	docker run -d --name money_mover -p 5000:5000 money_mover

pylint:
	pylint -j`nproc` app webapp money_mover
