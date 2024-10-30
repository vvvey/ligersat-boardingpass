# Generate LigerSat Boarding Pass with Pillow 
This is a webapp to generate a boarding pass for Ligersat nanosatellite project.
The application uses Flask to run the app, and Pillow to generate/edit the boarding pass template image.

This README provides instructions on how to set up and run a Flask application to generate LigerSat Boarding Pass.

## Prerequisites

- Python 3.x
- pip
- Docker (optional, if you choose to run via Docker)

## Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone git@github.com:vvvey/ligersat-boardingpass.git
cd ligersat-boardingpass
```

### 2. Install Dependencies
To install the required Python packages, run:

```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application
You can run the Flask application in one of two ways:

#### Option A: Run Locally
Start the Flask application using the following command:
```bash
python app.py
```
The application should be running on http://localhost:5000

#### Option B: Run Using Docker
If you prefer to run the application using Docker, you can build and run it with the following commands:

1. Build the Docker image
```bash
docker build -t ligersat:latest .
```
2. Run the Docker container:
```bash
docker run -d -p 5000:80 --name ligersat-app ligersat:latest
```
In this case, the application will also be available at http://localhost:5000

### 4. Demo

Check out Live Demo at http://ligersat.vvvey.me/

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Application Link: http://ligersat.vvvey.me
