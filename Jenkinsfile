pipeline {
    agent {
        label 'master'
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
