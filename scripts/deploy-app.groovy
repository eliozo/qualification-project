pipeline {
    agent any
    stages {
        stage('Execute Script') {
            steps {
                sh '''
                pwd
                git clone https://github.com/eliozo/qualification-project.git 
                cd qualification-project
                git pull origin main
                pwd
                cd /etc/our-flasks/eliozo
                pwd
                rm -fr *
                pwd
                cp -r /var/lib/jenkins/workspace/pipeline-deploy/qualification-project/eliozoapp/* .
                sudo systemctl stop eliozo.service
                sudo systemctl restart nginx
                sudo systemctl start eliozo.service
                '''
            }
        }
    }
}
