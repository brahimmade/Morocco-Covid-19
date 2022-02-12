<div id="top"></div>

<!-- PROJECT LOGO -->
<br />

<!-- TABLE OF CONTENTS -->
<details>
	<summary>Table of Contents</summary>
	<ol>
		<li>
			<a href="#about-the-project">About The Project</a>
			<ul>
				<li><a href="#built-with">Built With</a></li>
			</ul>
		</li>
		<li>
			<a href="#getting-started">Getting Started</a>
			<ul>
				<li><a href="#prerequisites">Prerequisites</a></li>
				<li><a href="#installation">Installation</a></li>
			</ul>
		</li>
		<li><a href="#usage">Usage</a></li>
		<li><a href="#roadmap">Roadmap</a></li>
		<li><a href="#contributing">Contributing</a></li>
		<li><a href="#license">License</a></li>
		<li><a href="#contact">Contact</a></li>
		<li><a href="#acknowledgments">Acknowledgments</a></li>
	</ol>
</details>

# Requirements 
1. Python 

# Running
1. download the zip archive of the repo or clone it
2. unzip the file and cd into it : 
```unzip morocovid--master; cd morocovid--master```
3. create a virtual environment for the project
 ```python -m venv env```

4. activate the environment by running :
```env\Scripts\activate```

5. install the requirements : 
```pip install -r requirements.txt```

6. run the project : 
```python main.py```

# Results

1. **covid-19 statistics per city, in CSV format** :  
The results are generated in the folder CSVs, 
the link is : https://github.com/moun3imy/morocovid/blob/master/CSVs/corona_{day}-{month}-{year}.csv  
*day*, *month* and *year* should be provided in two digit format, without any leading zeros in case it's a single digit

2. **covid-19 statistics nationally** :

execute : ```python read_stats.py ```  
this script will generate a dictionary containing all necessary statistics about COVID-19 on a national level

3. **generate all coronavirus-2 data for today** : 

execute : ```python .\covid_stats_json.py```  
this script will generate a dictionary containing all coronavirus-2 data for today

