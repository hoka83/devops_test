pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/hoka83/devops_test.git'
            }
        }

        stage('Set up Python environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
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
