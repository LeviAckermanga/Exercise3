pipeline {
    agent {
        kubernetes {
            label 'any'
            defaultContainer 'python'
            yaml """
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                some-label: some-label-value
            spec:
              containers:
                - name: python
                  image: python:3.8
                  command: ['python', 'app.py']  // Cambio aquí
            """
        }
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
