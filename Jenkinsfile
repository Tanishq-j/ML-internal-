pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub repository...'
                git branch: 'main', url: 'https://github.com/Tanishq-j/ML-internal-.git'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running Pytest test cases...'
                sh 'pytest -v tests/'
            }
        }

        stage('Docker Build & Run') {
            steps {
                echo 'Building Lightweight Python Docker image...'
                sh 'docker build -t hello-mlops-app:latest .'
                echo 'Running Container...'
                sh 'docker run --rm hello-mlops-app:latest "DevOps UAT"'
            }
        }

        stage('Evidently AI Monitoring') {
            steps {
                echo 'Running Evidently Model & Data Drift Monitoring...'
                sh 'python evidently_monitor.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
        success {
            echo 'UAT Dry Run: All stages passed successfully!'
        }
        failure {
            echo 'UAT Dry Run: Pipeline encountered errors.'
        }
    }
}
