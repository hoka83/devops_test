pipeline {
    agent any

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
                bat 'python -m venv $VENV_DIR'
                bat './$VENV_DIR/bin/pip install --upgrade pip'
                bat './$VENV_DIR/bin/pip install -r requirements.txt'
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
                bat 'nohup ./$VENV_DIR/bin/python app.py &'
                echo 'Flask app started!'
            }
        }
    }
}
