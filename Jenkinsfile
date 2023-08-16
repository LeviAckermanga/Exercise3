pipeline {
    agent {
        label 'principal'
    }
    
    stages {
        stage('Construir y Ejecutar') {
            steps {
                script {
                    bat 'python app.py'
                }
            }
        }
    }
}

}
