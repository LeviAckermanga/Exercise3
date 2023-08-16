pipeline {
    agent {
        label 'agent1'
    }
    
    stages {
        stage('Construir y Ejecutar') {
            steps {
                script {
                    container('python') {
                        sh 'python app.py'
                    }
                }
            }
        }
    }
}
