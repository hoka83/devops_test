pipeline {
    agent any

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
