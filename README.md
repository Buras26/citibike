# Citi Bike Jersey City Data Analysis Project

This project analyzes **Citi Bike Jersey City trip data** using Python notebooks.

**The project includes:**

- Downloading Citi Bike Jersey City data
- Cleaning and enriching trip data
- Collecting weather data
- Creating visualizations
- Performing neighborhood-level geospatial analysis

---

## Project Structure

```text
.
├── README.md
├── data
│   └── JC
└── notebooks
    ├── 1_Download_Citibike_Jersey_Data copy.ipynb
    ├── 2_Data_Enrichment.ipynb
    ├── 3_Weather_Data.ipynb
    ├── 4_Data_Visualization.ipynb
    └── 5_Neighborhood_Analysis copy.ipynb
```



## 1. Create a GitHub Repository

1. Go to GitHub.
2. Click **New repository**.
3. Enter a repository name, for example: `citibike`
5. Choose **Public**
6. Click **Create repository**.

If the project already exists locally, do not initialize the repository with a README file.

---

## 2. Clone the Repository

Open the terminal and run:

```bash
git clone https://github.com/YOUR_USERNAME/citibike.git
```

Replace `YOUR_USERNAME` with your GitHub username.

Navigate into the project folder:

```bash
cd citibike
```

---

## 3. Open the Project in VS Code

Open the project folder in VS Code:

```bash
code .
```

If the `code` command does not work, open VS Code manually and select:

```text
File → Open Folder → citibike-jersey-city-analysis
```

---

## 4. Create a Virtual Environment

Create a Conda environment:

```bash
conda create -n citibike-env python=3.12
```

Activate the environment:

```bash
conda activate citibike-env
```

---

## 5. Install Required Packages

Install the required Python packages:

```bash
conda install pandas geopandas folium plotly matplotlib ipykernel requests
```

When opening notebooks in VS Code or Jupyter, select this kernel:

```text
Python (citibike)
```

---

## 6. Recommended `requirements.txt`

Create a file named `requirements.txt`:

```text
pandas
geopandas 
folium 
plotly 
matplotlib 
ipykernel 
requests
```

Install packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 7. Data Folder

The project stores data inside:

```text
data/JC
```

This folder is used for Jersey City Citi Bike datasets.

Raw data files should be placed or downloaded into this folder.

---

## 8. Notebook Explanation

The notebooks should be executed in order.

---

### Notebook 1: `1_Download_Citibike_Jersey_Data copy.ipynb`

This notebook downloads Jersey City Citi Bike trip data.

Main tasks:

- Defines the required time periods
- Builds download URLs for Citi Bike data
- Downloads ZIP or CSV files
- Extracts downloaded files
- Saves raw data into the `data/JC` folder

Run this notebook first because the other notebooks depend on the downloaded data.

---

### Notebook 2: `2_Data_Enrichment.ipynb`

This notebook cleans and enriches the raw Citi Bike data.

Main tasks:

- Loads the downloaded trip data
- Cleans column names
- Converts date and time columns
- Creates new date-related fields
- Adds features such as year, month, weekday, and season
- Prepares the dataset for analysis

This notebook transforms raw data into an analysis-ready format.

---

### Notebook 3: `3_Weather_Data.ipynb`

This notebook prepares weather data for Jersey City.

Main tasks:

- Collects daily weather data
- Processes temperature, rain, snow, precipitation, and wind fields
- Aligns weather data with Citi Bike trip dates
- Prepares weather data for joining with ride activity

This notebook helps analyze the relationship between weather and Citi Bike usage.

---

### Notebook 4: `4_Data_Visualization.ipynb`

This notebook creates visualizations for the project.

Main tasks:

- Analyzes ride volume over time
- Creates daily, monthly, and seasonal charts
- Compares ride activity with weather indicators
- Builds visual outputs using libraries such as Matplotlib, Seaborn, Plotly, and Folium
- Supports exploratory data analysis and storytelling

This notebook is focused on visual analysis.

---

### Notebook 5: `5_Neighborhood_Analysis copy.ipynb`

This notebook performs neighborhood-level geospatial analysis.

Main tasks:

- Uses station coordinates
- Uses Jersey City neighborhood boundaries
- Maps Citi Bike stations to neighborhoods
- Aggregates rides by neighborhood
- Creates map-based visualizations
- Uses GeoPandas, Shapely, and Folium for spatial analysis

This notebook helps understand Citi Bike usage across different neighborhoods.

---

## 9. Suggested Notebook Execution Order

Run the notebooks in the following order:

```text
1_Download_Citibike_Jersey_Data copy.ipynb
2_Data_Enrichment.ipynb
3_Weather_Data.ipynb
4_Data_Visualization.ipynb
5_Neighborhood_Analysis copy.ipynb
```

The order is important because later notebooks depend on outputs from earlier notebooks.



## 10. Project Goal

The goal of this project is to analyze Jersey City Citi Bike usage patterns and understand how ridership changes by:

- Time
- Season
- Weather conditions
- Stations
- Neighborhoods

The project can be used for data analysis practice, geospatial analytics, dashboard preparation, and storytelling with real-world transportation data.