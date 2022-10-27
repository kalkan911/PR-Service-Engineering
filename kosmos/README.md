# KOSMOS Quickstart

This repository contains docker images and a docker-compose file to get you started fast with KOSMOS.

## Prerequisites

Please make sure you have Docker installed and running on your machine. Docker Desktop is available for Mac, Windows and Linux: https://www.docker.com/

## Get Started

### 1. Dowload the `docker-compose.yml` File

Download the `docker-compose.yml` file from the repository and save it in a folder.

### 2. Copy & paste the `.env` File

In the same folder you saved the `docker-compose.yml` file, please paste the provided `.env` file which contains the credentials for the databases.

### 3. Login to the Container Registry

You have to login to the container registry on GitLab to be allowed to pull any docker images from this repository.
Please open a terminal and execute following command. Make sure to replace `<USERNAME>` and `<DEPLOYMENT_TOKEN>` with the provided login credentials.

```
docker login registry.gitlab.com -u <USERNAME> -p <DEPLOYMENT_TOKEN>
```

### 4. Run KOSMOS

Open a terminal and navigate to the folder where your docker-compose.yml file is located.
Once you are in the folder, execute following command to start KOSMOS:

```
docker compose up
```

This will start all services (docker containers) for the KOSMOS application. It can take some time until all services started. Once KOSMOS is running, the UI is available at http://localhost:5000/.

If you want to run KOSMOS in the background, please use following command:
```
docker compose up -d
```

And this command to stop:
```
docker compose down
```
