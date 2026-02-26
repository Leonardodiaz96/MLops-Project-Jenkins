@Library('jenkins-shared') _

pipeline {
    agent any
    environment {
        DOCKER_REPO="leonardodiaz96/jenkins-shared-mlops-project"
    }
    stages {
        stage('Checkout') {
            steps {
                 gitCheckout('https://github.com/Leonardodiaz96/MLops-Project-Jenkins.git', '*/main', 'github-token')   
            }
        }

        stage('Build & Push Image') {
            steps {
                 dockerBuildAndPush(DOCKER_REPO, 'dockerhub-token')
            }
        }

        stage('Install Kubectl') {
            steps {
                 installKubectl()
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                 k8sDeploy('kubeconfig', )
            }
        }
    }
}