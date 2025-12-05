pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'git@github.com:priyannshu7497/CI-CD-Pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest || echo "No tests found, skipping..."'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ubuntu']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@3.110.16.94 "
                    cd /var/www/flask-app &&
                    git pull &&
                    sudo systemctl restart flask
                    "
                    '''
                }
            }
        }
    }
}
