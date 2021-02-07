#### To run the application locally

## 1. Pre-requisites
 - Anaconda installed locally
 - Helm installed locally

## 2. Set up venv
    git clone https://github.com/syashfr/ozar-designspace.git
    
    cd ozar-designspace  

    conda create --name <mylocalenv> --file conda_win.yml

    conda activate <mylocalenv>

## 3. Run App
    python manage.py runserver 
 

Ensure kubernetes cluster with the name ozards-d-aks is deployed and user namespace is created before making requests.