IMAGE_NAME=sdg-test-api
CONTAINER_NAME=sdg-test-container
PORT=8000

.PHONY: build run test stop clean

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --name $(CONTAINER_NAME) -p $(PORT):8000 $(IMAGE_NAME)

test:
	docker run --rm $(IMAGE_NAME) python django_project/manage.py test app.tests

stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

clean:
	docker system prune -f