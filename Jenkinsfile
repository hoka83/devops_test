pipeline {
    agent any
    tools {
        python 'Python3'  // Must match name in Jenkins Global Tool Config
    }
    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/hoka83/devops_test.git'
            }
        }

        stage('Set up Python environment') {
            steps {
                sh 'python -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install --upgrade pip'
                sh './$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Add test scripts later if needed
                echo 'No tests yet'
            }
        }

        stage('Deploy (Run Flask App)') {
            steps {
                sh 'nohup ./$VENV_DIR/bin/python app.py &'
                echo 'Flask app started!'
            }
        }
    }
}
