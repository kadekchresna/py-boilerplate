
pg:
	docker volume create v-pg-boilerplate && \
	docker run --name pg-boilerplate -e POSTGRES_PASSWORD=admin -d \
	-v v-pg-boilerplate:/var/lib/postgresql/data -p 5432:5432 \
	postgres:16

init:
	uv sync