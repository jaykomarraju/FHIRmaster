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
- Clone the repository:

`git clone https://github.com/yourusername/FHIRmaster.git`

- Install the Python dependencies:

`cd FHIRmaster/backend
pip install -r requirements.txt
`

- Install the React dependencies:

`cd ../frontend
npm install
`
