# These are the python files used for preliminary cleaning and joining of the excel data into more easily parsed CSV files.

1. **prelim_cleaning.py** is the main file to run. It will take excel formatted files from the *data/raw* directory and save them into the *data/combined directory* as comma-separated text files (CSV).

2. **tidy.py** is a helper-class. It takes the wide-format excel data and helps transform it into a tidy (long-form, single data point per row) dataframe.

3. **druginfo.py** is a script which will take the smaller drug use information from the excel files in the *data/raw* folder and also save it as a CSV file in *data/combined directory*. It cleans some minor cleaning of duplicate values.
