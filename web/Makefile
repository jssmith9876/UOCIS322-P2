all: build run

build: 
	docker build -t jordan-smith-cis322-2 .

run:
	docker run -t -p 5678:5000 jordan-smith-cis322-2

start:
	docker start jordan-smith-cis322-2

stop:
	docker stop jordan-smith-cis322-2

clean:
	docker container rm jordan-smith-cis322-2
