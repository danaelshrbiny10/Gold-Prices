py_sources = src/
target_version = py311

build:
    docker build -t egp .

up:
    - docker run -p 8888:8888 egp

down:
    docker-compose down

up-build:
    docker-compose up --build

logs:
    docker-compose logs

clean:
    docker container prune
    docker image prune

info:
    docker info
