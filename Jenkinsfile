pipeline{
    agent { label 'Springpath-B1' }
    options { skipDefaultCheckout() }
    environment {
        TRITON_QA_PATH = "$WORKSPACE" + '/' + "$BUILD_NUMBER" + "/gitops-nginxhello"
    }
    stages{
        stage ('Checkout the flux repo') {
            steps{
                    checkout([$class: 'GitSCM',
                    branches: [[name: 'master']],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: 'RelativeTargetDirectory',
                                    relativeTargetDir: '$BUILD_NUMBER/gitops-nginxhello']],
                    userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/renuarun2000/gitops-nginxhello.git']],
                    credentialsId: 'github-my-credentials-id'])
                }
        }
        stage ('Create customer repo') {
            steps{
                 withCredentials([gitUsernamePassword(credentialsId: 'github-my-credentials-id')]) {
                     ws("$TRITON_QA_PATH"){
                     sh """
                         #!/bin/bash
                         git checkout master
                         git pull origin
                         echo "Processing manifest files for customer $Customer"
                         mkdir -p "Customers/$Customer"
                         python buildManifest/processCustomer.py $Customer
                         git add -A
                         git commit -m "Added a new customer"
                         git push origin master
                         echo "Creation of customer manifest for $Customer successful"
                     """
                 }
                 }
            }
        }
    }
}