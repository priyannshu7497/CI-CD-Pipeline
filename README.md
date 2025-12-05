📄 README.md (Copy-Paste Ready)
# 🚀 Flask CI/CD Pipeline Deployment on AWS EC2

### **📌 Student Details**
| Field | Information |
|-------|------------|
| Name | Priyanshu Gupta |
| College | Amity University |
| Project | CI/CD Pipeline with Jenkins & Flask |

---

## 📚 Project Overview

This project demonstrates a fully automated **CI/CD pipeline** using:

- **Flask (Python Web App)**
- **GitHub (Version Control)**
- **Jenkins CI/CD**
- **Gunicorn (Python WSGI Server)**
- **Nginx (Reverse Proxy & Production Web Server)**
- **AWS EC2 (Hosting)**

Whenever code is pushed to GitHub, Jenkins automatically:

✔ Pulls latest code  
✔ Installs dependencies  
✔ Restarts the application  
✔ Deploys updated version live  

---

## 🏗 Architecture



Developer → GitHub → Jenkins → Gunicorn → NGINX → User


---

## 🛠 Tech Stack

| Component | Tool |
|----------|------|
| Language | Python |
| Framework | Flask |
| CI/CD | Jenkins |
| Version Control | Git + GitHub |
| Web Server | Nginx |
| App Server | Gunicorn |
| Cloud | AWS EC2 |

---

## ⚙️ Setup & Deployment Steps

### **1️⃣ Launch EC2 Instance**
- Ubuntu 22.04
- Open ports: `22`, `80`, `8080`


sudo apt update && sudo apt upgrade -y

2️⃣ Install Python & Flask App
sudo apt install python3 python3-pip python3-venv -y
git clone <your-repo-url>
cd repo-folder
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Test locally:

python app.py

3️⃣ Install & Configure Jenkins
sudo apt install openjdk-17-jdk -y
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
   /usr/share/keyrings/jenkins-keyring.asc > /dev/null
sudo apt-get install jenkins -y


Enable Jenkins:

sudo systemctl enable --now jenkins


Login → Install plugins → Add GitHub Webhooks.

4️⃣ Configure Jenkins Pipeline

Add the following Jenkinsfile in the repo:

pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps { git 'https://github.com/username/repo.git' }
        }
        stage('Install Dependencies') {
            steps { sh 'pip install -r requirements.txt' }
        }
        stage('Restart Application') {
            steps { sh 'sudo systemctl restart flask' }
        }
    }
}

5️⃣ Install Gunicorn & Create Systemd Service
pip install gunicorn


Create service:

sudo nano /etc/systemd/system/flask.service

[Unit]
Description=Gunicorn running Flask app
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/var/www/flask-app
ExecStart=/var/www/flask-app/venv/bin/gunicorn --workers 3 --bind unix:/var/www/flask-app/flask.sock wsgi:app

[Install]
WantedBy=multi-user.target


Start service:

sudo systemctl daemon-reload
sudo systemctl start flask
sudo systemctl enable flask

6️⃣ Configure Nginx Reverse Proxy
sudo nano /etc/nginx/sites-enabled/flask

server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://unix:/var/www/flask-app/flask.sock;
        include /etc/nginx/proxy_params;
    }
}


Restart:

sudo systemctl restart nginx

🧪 Testing

Test locally:

curl http://localhost


Visit in browser:

http://<EC2-Public-IP>


Expected Output:

Hello from Flask CI/CD Pipeline!

📸 Screenshots
Item	Screenshot

<img src="https://raw.githubusercontent.com/priyanshu/CI-CD-Pipeline/Flask-CICD-Pipeline Screenshot/Jenkins Pipeline Success.png" width="600">

GitHub Repo	(Add Screenshot)
Nginx running	(Add Screenshot)
Browser Output	(Add Screenshot)
🎯 Final Deliverables

✔ Fully working CI/CD
✔ Auto deployment on push
✔ Secure + production ready
✔ Documented setup

🏁 Conclusion

This project demonstrates how modern development teams automate deployment workflows using:

CI/CD pipelines

Cloud hosting

Web server configuration

It improves deployment speed, reduces manual errors, and enables scalable production environments.

⭐ Author: Priyanshu Gupta
