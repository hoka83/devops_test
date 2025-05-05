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
        // Create the virtual environment
        bat 'python -m venv %VENV_DIR%'

        // Upgrade pip in the virtual environment
        bat 'call %VENV_DIR%\\Scripts\\activate.bat && pip install --upgrade pip'

        // Install dependencies from requirements.txt
        bat 'call %VENV_DIR%\\Scripts\\activate.bat && pip install -r requirements.txt'
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
