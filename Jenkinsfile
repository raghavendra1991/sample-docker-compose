// Declarative pipeline
pipeline {
    agent any

    stages {

        stage ('Git Checkout') {
            steps {
                git branch: 'feature', credentialsId: 'github', url: 'https://github.com/raghavendra1991/sample-docker-compose.git'
            }
        }
        
        stage ('Build Docker Image') {
            steps {
                sh 'docker-compose build '       
            }
        }
    }
}
