# alertlogic al-python38-amzn2 rpm for centos7/amzn2

### to register repo and deploy with codebuild
```bash
# to register repo
aws --region=us-east-1 --profile=dev-sysops-dsa cloudformation create-stack --stack-name ${MYREPO} --template-body file://pipeline_cfn.yml --capabilities CAPABILITY_NAMED_IAM

# to deploy to integration
aws --region=us-east-1 --profile=dev-sysops-dsa codebuild start-build --project-name ${MYREPO}

# to deploy to all mirrors, including production
aws --region=us-east-1 --profile=dev-sysops-dsa codebuild start-build --project-name ${MYREPO} --environment-variables-override name=PROD_RELEASE,value=RFC,type=PLAINTEXT
```

# developer notes
* rpm versioning is handled by git automagically (git describe --tags --long)
* the latest commit creates an rpm revision that obsoletes previous ones (older revisions will still be available)
* do not pin revisions in your cfn/chef recipes unless absolutely necessary (it breaks compliance)
* do not manually deploy rpms directly to mirrors (bad things will happen)
* never run createrepo or anything similar (bad things will happen)

### to test rpm build in docker
* see docker file in docker folder
