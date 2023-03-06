# FHIRmaster
FHIRmaster is a clinical decision support system that leverages FHIR and SNOMED CT to identify potential diagnoses and treatments based on patient data. It uses a Bayesian network to update the probabilities associated with each node and then calculates the probability of each potential diagnosis and treatment based on the updated probabilities. The system is built using Python, Flask, React, OpenCDS, CQL, ECL, and Firebase.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
- Python 3.7 or higher
- Node.js 14.0 or higher
- npm 6.14 or higher
- Firebase account and project

## Installing

1. Clone the repository:

```
git clone https://github.com/yourusername/FHIRmaster.git
```

2. Install the Python dependencies:

```
cd FHIRmaster/backend

pip install -r requirements.txt
```

3. Install the React dependencies:

```
cd ../frontend

npm install
```

4. Create a Firebase project and configure the credentials:

    - Go to the Firebase console and create a new project.
    - Click on the "Project settings" gear icon and then on the "Service accounts" tab.
    - Click on the "Generate new private key" button to download the JSON key file.
    - Rename the key file to firebase-credentials.json and copy it to the backend directory.
    - Edit the backend/config.py file and replace the <PROJECT_ID> placeholder with your Firebase project ID.



## Running

1. Start the backend:

```
cd backend

python app.py
```

2. Start the frontend:

```
cd ../frontend

npm start
```

3. Open the application in your browser:

```
http://localhost:3000/
```

## Built With

- Python - Backend programming language
- Flask - Web framework for Python
- React - Frontend JavaScript library
- OpenCDS - Clinical decision support system
- CQL - Clinical Quality Language
- ECL - Expression Constraint Language
- Firebase - Cloud services platform

Authors
Jay Komarraju - Initial work - [jaykomarraju](https://github.com/jaykomarraju)
