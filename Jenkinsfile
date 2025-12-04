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
                sh 'nohup ./venv/bin/python app.py > flask.log 2>&1 &'
            }
        }
    }

    post {
        success {
            echo '✅ Build succeeded. Sending success email...'
            mail to: 'your_email@gmail.com',
                 subject: "✅ Build Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: """\
Hello Swetabh,

Your Jenkins build **${env.JOB_NAME} #${env.BUILD_NUMBER}** succeeded.

🔗 View it here: ${env.BUILD_URL}

Regards,  
Jenkins CI/CD Bot
"""
        }

        failure {
            echo '❌ Build failed. Sending failure email...'
            mail to: 'your_email@gmail.com',
                 subject: "❌ Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: """\
Hello Swetabh,

Your Jenkins build **${env.JOB_NAME} #${env.BUILD_NUMBER}** has failed.

🔗 Check the logs: ${env.BUILD_URL}

Regards,  
Jenkins CI/CD Bot
"""
        }
    }
}
