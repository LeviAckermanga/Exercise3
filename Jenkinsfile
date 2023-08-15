pipeline {
    agent {
        docker {
            image 'python:3.8'
            args '-u root'
        }
    }
    
    stages {
        stage('Clonar Repositorio') {
            steps {
                checkout scm
            }
        }
        
        stage('Ejecutar Registro') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
