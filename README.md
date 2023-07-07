## Configuring Your Development Environment

### Configure your SSH and GPG Keys
These steps are not required, but highly recommended
- Connect to GitHub using the [Secure Shell Protocol](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- Use [GPG Keys](https://docs.github.com/en/authentication/managing-commit-signature-verification) to configure commit signature

### Install Docker
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or...
- - [Docker Engine](https://docs.docker.com/engine/install/)
- - [Docker Compose](https://docs.docker.com/compose/install/)

### Set your environment variables
- Create a new file named `.env` in the root folder
- Copy the content of the `.env.dev` file to the new `.env`
- Update the variable values with your preferences
- - When adding new keys, remember to pass it to `docker-compose.yml` and `.env.dev`
- - This helps others developers configuring and updating their development environment

### Create Python Virtual Environment
- Download and install [Python](https://www.python.org/downloads/) with your desired version
- Run `python<version> -m venv .venv` to create a new python virtual environment
- - You can choose other names than `.venv`, just be careful to avoid conflicts with `.env` file
- - Check [this docs](https://docs.python.org/3/library/venv.html) for more info about using venv module

### Install project dependencies
- Activate your virtual environment `.venv`
- Run `pip install poetry` and `poetry install --only main`
- After installing main dependencies, install dev dependencies
- Run `poetry install --only dev` and `pre-commit install`

### Run project
- Run `docker compose build && docker compose up -d`
- Go to http://localhost:5000/apidocs
- To stop, run `docker compose down`
