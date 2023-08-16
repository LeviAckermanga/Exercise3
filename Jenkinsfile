pipeline {
    agent {
        label 'windows'
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
