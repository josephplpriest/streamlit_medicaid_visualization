# Streamlit Medicaid/Medicare Data

## 1. A project to explore drug spending data from the US government.

## 2. Covering the years 2012-2020, including both Medicare (generally patients 65+) and Medicaid (by need).

## 3. Allow users to select a drug to find more information about its use







### How to run this project
Python>=3.8
Other requirements provided by dockerfile + requirements.txt

Install docker.

Clone the repo.

From the command line, in the repo folder, run:
```bash
docker build -t medi-app .
```
```bash
docker run -dit -p 8501:8501 medi-app
```
```bash
docker exec -it <container_name> /bin/bash
```
from the command line in the container run:
```bash
python cleaning.py
```
It may take a few seconds to run, then will print a notification when it's done

Next, run:
```bash
streamlit run app.py
```
Click on the network link or type into browser:

localhost:8501


After running the program, type Ctrl^C to close streamlit in the terminal and type "exit" to leave the docker container.

```bash 
docker kill <container_name>"```  <---- kill the container process

```bash 
docker container prune``` 	 <---- remove the container

```bash 
docker rmi -f <image_name>```   <---- remove the image, IMPORTANT as it will likely be 1+GB as it includes the full python distro + packages

### Alternatively, create a virtual env then install packages via requirements.txt

```bash
python3 -m venv medi-env
```

```bash
pip install -r requirements.txt
```
```bash
python cleaning.py
```
It may take a few seconds to run, then will print a notification when it's done

Next, run:
```bash
streamlit run app.py
```
Click on the network link or type into browser:

localhost:8501


## Project Requirements:

1. 
