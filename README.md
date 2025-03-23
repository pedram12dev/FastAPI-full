# the fastapi project with docker,sqlmodel,sqlalchemy,pydantic and more ...

# all endpoint tests by 'requests' package (in nbs folder).



## Docker 

- `docker build -t fast-api:v1 -f Dockerfile .`
- `docker run -it fast-api:v1`

## Docker compose 

add watch in docker compose if change code or installed package , automaticlly restart docker engine
and run server.
- `docker-compose up --watch`
- `docker-compose down`