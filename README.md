# Square-of-the-number

The simple realization of getting square of given number through API

## Roadmap

- [x] Determine a needed tool for developing.
- [x] Write a first endpoint.
- [x] Configure a celery instance
- [x] Write a celery task to calculate square of the selected number
- [x] Add a tool for monitoring celery tasks and workers
- [x] Cover a feature by tests
- [x] Set up existing feature inside docker
- [ ] Add a database tools.

## How it works

### Developer commands

- You need a docker and docker-compose on your machine.
   - https://docs.docker.com/engine/install/ubuntu/
    - https://docs.docker.com/compose/install/
- `make run`. Use this command if you have to use API.
- `make clear`. If you had to finish working on.

#### Tests

- `make tests`


### API
Please open http://127.0.0.1:5050/docs to get to know about existing endpoints
