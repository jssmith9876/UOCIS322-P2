IMG=jordan-smith-cis322-2
PORT=5678


all: build run

build: 
	docker build -t $(IMG) .

run:
	docker run -t -p $(PORT):5000 $(IMG)

start:
	docker start $(IMG)
	
stop: 
	docker stop $(docker ps --format "{{.Names}}" --filter ancestor=$(IMG))

clean:
	docker container rm jordan-smith-cis322-2
