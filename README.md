# Streamlit Medicaid/Medicare Data

## 1. A project to explore drug spending data from the US government.

What drugs are the most expensive?
Are they due to a certain subsection of conditions?
What drugs have the highest demand (most claims)?
What drug companies are making the most money from Medicare/Medicaid?


## 2. Covering the years 2012-2020, including both Medicare (generally patients 65+) and Medicaid (by need).

## 3. Allow users to select a drug to find more information about

# How to run this project

Install docker.

Clone the repo.

From the command line, in the repo folder, run:

docker build -t medi-app .

docker run -dit -p 8501:8501 medi-app

docker exec -it <container_name> /bin/bash

# from the command line in the container run:

python cleaning.py

#It may take a few seconds to run, then print a notification when it's done

#Next, run

streamlit run app.py

#Click on the network link or type into browser:

localhost:8501


#After running the program, type Ctrl^C to close streamlit in the terminal and type "exit" to leave the docker container.
"docker kill <container_name>"  <---- kill the container process

"docker container prune" 	 <---- remove the container

"docker rmi -f <image_name>"   <---- remove the image, IMPORTANT as it will likely be 1+GB as it includes the full python distro + packages
