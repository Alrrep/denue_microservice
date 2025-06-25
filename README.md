# 🗺️ DENUE Microservice

Microservice for searching and visualizing commercial establishments using INEGI’s DENUE API.

## 📋 Tabla de Contenidos

- [Description](#description)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)
- [Testing](#testing)
- [LInks](#links)
- [Support](#support)

## 📖 Description

This microservice enables users to search for commercial establishments (restaurants, pharmacies, banks, etc.) within a specific radius of geographic coordinates using the DENUE (National Statistical Directory of Economic Units) API provided by INEGI.

### Funcionalidades principales:
- Search by geographic coordinates
- Filter by type of establishment
- Interactive map visualization
- Automatic geolocation
- Responsive web interface

## ✨ Features

- **Microservice**: Container-based architecture
- **REST API**: Well-structured endpoints
- **Interactive maps**: Visualization using Folium
- **Responsive**: Mobile-friendly design
- **Dockerized**:  Easy deployment and scalability
- **Testing**: Complete test suite
- **CI/CD**: Continuous integration via GitHub Actions

## 🏗️ Architecture

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   External API  │
│   (Templates)   │◄──►│   (Flask App)   │◄──►│   (DENUE API)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │
         │                       │
         ▼                       ▼
┌─────────────────┐    ┌─────────────────┐
│   Static Files  │    │   Configuration │
│   (CSS)         │    │   (Environment) │
└─────────────────┘    └─────────────────┘



## 🚀 Installation

### Prerequisites
- Python 3.11+
- Docker and Docker Compose
- DENUE API Token (INEGI)
- Git 

### Local Setup

1. **Clone the repository:**

bash
git clone https://github.com/Alrrep/denue_microservice.git
cd denue_microservice



2. **Create a virtual environment:**

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



3. **Install dependencies:**

bash
pip install -r requirements.txt



4. **Configure environment variables:**

bash
cp .env.example .env
# Edit the .env file with your DENUE token



5. **Run the application:**

bash
python app.py


## 🐳 Docker

### Development with Docker Compose

bash
# Build and run the container
docker-compose up --build



## 🔧 Usage

### Web Interface

1. Go to http://localhost:5000
2. Enter latitude and longitude
3. Select the type of establishment
4. Define the search radius
5. Click on Search Establishments

### API REST

bash
# Buscar establecimientos
curl "http://localhost:5000/buscar-coordenadas?latitud=19.656454&longitud=-101.219097&distancia=2000&condicion=restaurante&condicion="



## 📚 API Endpoints

### GET /
- **Description**: Main page with search form
- **Response**: HTML template

### GET /buscar-coordenadas
- **Description**: Buscar establecimientos por coordenadas
- **Parameters**:
  - latitud (float, required): Latitude
  - longitud (float, required): Longitude
  - distancia (int, optional): Radius in meters (default: 1000)
  - condicion (string, optional): Type of establishment (default: "todos")

**Example of successful response:**

html
<!-- HTML template with map and results -->


## 🧪 Testing
This project was successfully tested on an AWS EC2.
The application was deployed and accessible at: http://<public-ip>:5000

Steps followed:
1. Created EC2 instance with Ubuntu 22.04
2. Installed Docker and Docker Compose
3. Cloned the repository
4. Added .env file with DENUE token
5. Ran docker-compose up --build

## 📝 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE.txt) file for details.

## 🔗 Links

- [API DENUE](https://www.inegi.org.mx/servicios/api_denue.html)
- [Documentación Flask](https://flask.palletsprojects.com/)
- [Folium Documentation](https://python-visualization.github.io/folium/)

## 📞 Support

Para soporte técnico:
- 📧 Email: perlaa.rmn@gmail.com