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
                bat 'python -m venv %VENV_DIR%'
                bat '''
curl https://bootstrap.pypa.io/pip/3.8/get-pip.py -o get-pip.py
call %VENV_DIR%\\Scripts\\activate.bat && python get-pip.py
call %VENV_DIR%\\Scripts\\activate.bat && pip install --upgrade pip
call %VENV_DIR%\\Scripts\\activate.bat && pip install -r requirements.txt
'''
            }
        }

             stage('Run Script') {
            steps {
                // Run the Python script inside the virtual environment
                bat 'call %VENV_DIR%\\Scripts\\activate.bat && python test.py'
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
                bat 'nohup ./$VENV_DIR/bin/python test.py &'
                echo 'Flask app started!'
            }
        }
    }
}
