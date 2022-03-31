# Streamlit Medicaid/Medicare Data
### A project to explore US drug spending data, covering the years 2012-2020, including both Medicare part D (generally for patients 65+) and Medicaid (by need).


## Project Requirements:

### 1. Python programming basics:
  
  a. The streamlit **app.py** runs as a loop, updating when the user gives an input or changes a value (selecting a drug for instance)
  
  b. **Tidy.py** contains the **tidy** class that is imported into **cleaning.py** in order to convert the excel files to tidy dataframes.
  
  c. The **tidy** class uses lists to keep track of the split dataframes, before gluing them together/appending them.
  
  d. The *tidy.set_indices*, *tidy.set_values* and *tidy.glue* are three defined methods. The *set_indices* saves state data in the class (indices for multiple dataframes), the second saves multipe dataframes in a list, and the third returns a complete dataframe with shared indices.

### 2. Utilize External Data:
  
  a. Data is taken from:
  
  https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicaid-spending-by-drug
  
  https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-d-spending-by-drug/data
  
  b. Using excel files, the **cleaning.py** file reads in the excel files, using separate sheets from each, and combines the data, saving it as two csvs, **cleaned.csv** and **drug_info.csv**.

### 3. Data Display:
  
  a. Using the streamlit **app.py**, we display data for the years 2012-2020 with plotly. Currently, we are showing "Total Dosage Units" vs "Total      Spending", with labels according to the drugs' "Brand Name."
  
  b. The user can search for drug info by "Generic" or "Brand" name. Using fuzzy matching and the Levenshtein distance to return the closest drug names, we search the drug info database for the closest matches and display descriptions of the drug, as well as tabular info regarding spending.
  
### 4. Best Practices:
  
  a. Using a dockerfile, we can have the user get an identical image and container to run the programs.
  
  b. Alternatively, we have included documentation for using a virtual environment and the **requirements.txt** file to run the programs.
  
### 5. "Stretch" List:
  
  a. TBD unit testing
  
  b. There are two minimal jupyter notebooks in the repo under the notebooks directory. More analysis and possibly data cleaning is needed.



## How to run this project
Python>=3.8
Other requirements provided by dockerfile + requirements.txt

#### Install docker.

#### Clone the repo.

From the command line, in the repo folder, run:
```bash
docker build -t medi-app .
```
```bash
docker run -dit -p 8501:8501 -p 8888:8888 medi-app
```


After running, this will print the container name, to use in the next line. Alternatively, use "docker ps" to see the simpler name given by docker to the container. We map the host machine ports to the container ports 8501 and 8888 to access the streamlit app and jupyter outside the container.

```bash
docker exec -it <container_name> /bin/bash
```
from the command line in the container run:
```bash
python src/prelim_cleaning.py
```
It may take a few seconds to run, then will print a notification when it's done

You can then run the jupyter notebooks, in the notebook folder, using:

```bash
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```

Access the jupyter notebook in the browser with the "http://127.0.0.1:8888/?token=" that jupyter prints to the console.

Note, the jupyter notebooks must be run in order to have the correct data.

Next, run:
```bash
streamlit run app.py
```

Click on the network link or type into browser:

localhost:8501


After running the program, type Ctrl^C to close streamlit in the terminal and type "exit" to leave the docker container.

```bash
docker kill <container_name>
```  
^^ this will kill the container process

```bash
docker ps
```
(if you've forgotten the container name)

```bash
docker container prune
``` 	
^^ remove the container

```bash
docker rmi -f <image_name>
```
```bash
docker images
```
(if you've forgotten the container name)

^^ remove the image, IMPORTANT as it will likely be 1+GB as it includes the full python distro + packages

### Alternatively, create a virtual env then install packages via requirements.txt

```bash
python3 -m venv medi-env
```

```bash
source medi-env/bin/activate
```

```bash
pip install -r requirements.txt
```
```bash
python src/prelim_cleaning.py
```
It may take a few seconds to run, then will print a notification when it's done

```bash
jupyter notebook
```
To run the notebooks. (Note: They must be run in order, after running **src/prelim_cleaning.py**)

Next, run:
```bash
streamlit run app.py
```
Click on the network link or type into browser:

localhost:8501



