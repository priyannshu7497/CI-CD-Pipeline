pipeline {
    agent any

    environment {
        VENV_DIR = "./venv"
    }

    stages {

        stage('Build') {
            steps {
                echo '🔧 Creating virtual environment and installing dependencies...'
                sh 'python3 -m venv $VENV_DIR'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                sh './venv/bin/python -m pytest'
            }
        }

        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo '🚀 Deploying Flask app...'
                sh 'pkill -f app.py || true'
                sh 'nohup ./venv/bin/python app.py > flask.log 2>&1 &'
            }
        }
    }

    post {
        always {
            echo "🎉 Pipeline Completed!"
        }
    }
}
