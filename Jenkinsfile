pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('2').username
        AWS_SECRET_ACCESS_KEY = credentials('2').password
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/hoka83/devops_test.git'
            }
        }


   
       stage('Terraform Init') {
      steps {
          withCredentials([usernamePassword(credentialsId: '2', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    bat 'terraform init'
                }
        
      }
    }

    stage('Terraform Plan') {
      steps {
                          withCredentials([usernamePassword(credentialsId: '2', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    bat 'terraform plan'
                }
        
      }
    }

    stage('Terraform Apply') {
      steps {
                        withCredentials([usernamePassword(credentialsId: '2', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
        bat 'terraform apply -auto-approve'
                }
        
      }
    }
}
}
