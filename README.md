# API Automation with Karate

This project is designed to automate API testing using Karate framework. It generates feature files for all API endpoints defined in a Swagger document and a Postman collection.

## Setup Instructions

1. Clone the repository.
2. Install the necessary dependencies using the `requirements.txt` file.
3. Ensure you have the Karate framework set up.
4. Run the `setup.py` script to initialize the project.

## How to Use

1. Place your Swagger document (`swagger.yaml`) and Postman collection in the designated folders.
2. Run the automation script `generate_tests.py` to generate the feature files.
3. The generated feature files will be in the `features` directory.
4. Execute the feature files using the Karate command line or your preferred CI/CD pipeline.

## Directory Structure

- `datafiles/petstore`: Contains JSON files for expected requests and responses.
- `features`: Contains the generated feature files.
- `schemas`: Contains JSON schema files for response validation.
- `scripts`: Contains utility scripts for generating feature files.
