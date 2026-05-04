# Capstone_Project_Charles-Simpson_Thailand-Griffith
# Title: A Dying Planet
# This repository aims to center around how climate change is getting worst in the world throughout the years.

# Planning: The purpose of this project is to highlight the rise of climate change, specifically global warming throughout the world, how different countries are being affected by it, how the weather is being affected by global warming/climate change, and how worse the condition is getting. By taking the data from the CSV file provided from Kaggle.com, Thailand and I intend to visualize the data from the dataset into an interactive graph where viewers are able to see the effect of climate change that has occurred throughout the years and how every country in the world is affected by it.

# To achieve achieve this, Thailand and I will be splitting the work into two: Thailand will be responsible for the backend development of the code, where he will implement FastAPI/SQLite to code the data to present it within a database, he will also manage the data utilizing Google Cloud Storage to copy the code that we used to create the visuals from Github, finally, he will test the code and the data to make sure everything works properly. As for me, I will working on the frontend development of the data where I will create the Steamlit dashboard, all of the visualizations for the data, including interactive graphs, and creating the CI/CD setup for the entire project.

# All of the code for the project will be performed within the shared GitHub Codespaces Repository. To properly sort through all of the code, three files were created:

# 1: docs: This folder will serve as a way to document all of the findings from the CSV file.
# 2: diagrams: This folder will be utilized to store the visualizations of all of the diagrams that are produced from the repository/the local server.
# 3: src: This final folder will be utilized to insert all of the code that is implemented to create the final product.

# The target charts that we are aiming to use for this project include a graph with a slider that allows the viewer to slide an arrow/dot through the years to see how climate change changed over time, how it affected the countries and what it is doing to the weather around the world. The second graph we are planning on incorporating is a line chart that displays a timeline of the effects of climate change as time went on. After inserting the data from the CSV file and writing the code to create the desired graphs, Thailand will copy all of the code into Google Cloud Storage. As for the potential API endpoints we plan on utilizing, we are planning on using endpoints such as /data/GET, /data/POST, and /data/DELETE to name a few. Finally as for the database schema, the main purpose of it will be to correlate the specific causes of climate change to the overall effect and how the world is being affected by it over time.

# Overall, the final outcome of the data should showcase the direct causes towards the worsening condition of climate change and start to offer some solutions of how we can work to try to lessen the damage already caused.

# Part 1: SETUP
Step 1: Create the diagram, docs, src, tests, and requirements.txt files.
1. mkdir diagram
2. mkdir docs
3. mkdir src
4. mkdir tests
5. touch requirements.txt
Step 2: Set up the dependencies in requirements.txt:
fastapi
uvicorn
pandas
pytest
httpx
flake8
google-cloud-storage
autopep8
streamlit
plotly
requests
sqlalchemy
# Part 2: BACKEND DEVELOPMENT
Step 1:
# Part 3: FRONTEND DEVELOPMENT
Step 1:
# Part 4: TESTING AND CODE QUALITY
Step 1: With flake8 and pytest installed from the rest of the dependencies, enter flake8 <file_name> into the terminal to highlight any and all issues within the code.
Step 2: Install pytest by entering: pip install pytest pytest-hhtpx into the terminal. Afterwards, write pytest test_backend.py to test how long it takes to fully load all of the data and the FastAPI endpoints.
# Part 5: CI/CD SETUP
Step 1: 
# Part 6: PERFORMANCE ANALYSIS
# Part 7: DOCUMENTATION