Healthcare Survey Web App
A Flask-based web application developed to collect and analyze income and expense data for healthcare product planning. The project includes data collection, storage, export, visualization, and deployment.

Live Demo
 https://healthcare-survey-app.onrender.com

Features
Web-based survey form (Age, Gender, Total Income, Expense Categories)

Data storage using MongoDB (via MongoDB Atlas)

Export collected data to CSV

Generate charts using Jupyter Notebook:

Ages with the highest income

Gender-based spending per category

Hosted on Render using Gunicorn and Python 3.11

Technologies Used
Flask – Web framework

MongoDB – NoSQL database for storage

pymongo – MongoDB connector

pandas, matplotlib, seaborn – Data analysis and visualization

Jupyter Notebook – Exploratory data analysis

Gunicorn – Production WSGI server for deployment

Render – Cloud platform for hosting

Project Structure

survey_tool_fresh/
├── app.py                  # Flask app
├── templates/
│   └── form.html           # Survey form template
├── export_to_csv.py        # MongoDB to CSV export
├── data.csv                # Exported data
├── analysis.ipynb          # Jupyter notebook with charts
├── requirements.txt        # Dependencies
├── render.yaml             # Render deployment config
└── README.md               # Project overview

How to Run Locally
1. Clone the repository
git clone https://github.com/yourusername/healthcare-survey-app.git
cd healthcare-survey-app

3. Set up a virtual environment

python -m venv venv
venv\Scripts\activate     # Windows

4. Install dependencies
   
pip install -r requirements.txt

6. Run the Flask app

python app.py
Visit http://127.0.0.1:5000 in your browser.

How to Analyze the Data
Submit data through the live or local form

Run:

python export_to_csv.py
Open analysis.ipynb in Jupyter Notebook to generate visual insights

Deployment Notes (Render)
gunicorn app:app used as the start command

render.yaml configures the web service

App is live and public at the Render-provided URL

License
This project was developed as a final assignment for data analysis training.
© 2025 Yetunde Salami. All rights reserved.

