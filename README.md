Introduction
This is a sample solution using a SageMaker pipeline.  This implementation could be useful for any organization trying to automate their use of Machine Learning.  With an implementation like this, any inference is easy, and can simply be queried through an endpoint to receive the output of the model’s inference, tests can be automatically performed for QA, and ML code can be quickly updated to match needs.

Prerequisites
- AWS account – Follow these instructions to create an AWS Account: http://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/AboutAWSAccounts.html
- EC2 Key Pair – Follow these instructions to create an EC2 Key Pair: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair
- GitHub OAuth Token – Follow these instructions to create an OAuth Token: https://github.com/stelligent/devops-essentials/wiki/Prerequisites#create-an-oauth-token-in-github

Architecture and Implementation
  Architecture Diagram
  (TO BE CREATED)

  Components details
  - AWS CloudFormation – This solution uses the CloudFormation Template language, in either YAML or JSON, to create each resource.
  - AWS CodeBuild – This solution uses CodeBuild to build the source code from GitHub
  - AWS CodePipeline – CodePipeline has various stages defined in CloudFormation which step through which actions must be taken in which order to go from source code to creation of the production endpoint.
  - AWS EC2 – EC2 Instances are created in order to train the model as well as host the model to be accessed via and endpoint.  
  - AWS SageMaker – This solution uses SageMaker to train the model to be used and host the model at an endpoint, where it can be accessed via HTTP/HTTPS requests
  - AWS IAM – Separate Identity and Access Management (IAM) Roles are created for the pipeline, CodeBuild, and CloudFormation.
  - AWS SNS – This solution uses a Simple Notification Service (SNS) Topic in order to approve movement into production after testing.
  - AWS S3 – Artifacts created throughout the pipeline as well as the data for the model is stored in an Simple Storage Service (S3) Bucket.

CloudFormation Template(s) resources
  - AWS CloudFormation – AWS::CloudFormation::Interface sets parameter group metadata.
  - AWS CodeBuild – AWS::CodeBuild::Project uploads the project source code stored in GitHub to an S3 bucket.
  - AWS CodePipeline – AWS::CodePipeline::Pipeline – Easiest to create the Pipeline in the AWS Console, then use the get-pipeline CLI command to get the configuration in JSON to be placed into the CloudFormation Template.
  - AWS EC2 – (instance type specified in AWS::SageMaker::EndpointConfig)
  - AWS SageMaker – AWS::SageMaker::Model – here the algorithm to be used by SageMaker is specified, as well as the source code to be submitted to once the model has been created;
    AWS::SageMaker::Endpoint – this is the endpoint from which you can make requests;
    AWS::SageMaker::EndpointConfig – here we specify key configurations for the endpoint, including the type of EC2 instance used, and can specify if we would like multiple endpoint models, e.g. for A-B testing, and similarly how much/what traffic we will direct to this endpoint.
  - AWS IAM – AWS::IAM::Role – Make sure to specify only the necessary permissions for each role.
  - AWS SNS – AWS::SNS::Topic sends a confirmation to the email specified as a parameter.
  - AWS S3 – AWS::S3::Bucket

Costs
- CloudFormation – No Additional Cost
- CodeBuild – Charges per minute used. First 100 minutes each month come at no charge.
- CodePipeline – $1 per month per pipeline
- EC2 – Hourly prices Vary based on size/type of instance used
- SageMaker – Prices vary based on EC2 instance usage for Building in Notebook Instances, Model Hosting, and Model Training; each charged per hour of use.
- IAM – No Additional Cost
- SNS – Realistically No Cost – Free for first 1 million SNS requests and for first 1,000 Email Deliveries each month.
- S3 – Prices Vary, depends on size of model/artifacts stored

Parameters
- PipelineName: The name of the Pipeline
- TemplateFileName: The file name of the SageMaker CloudFormation template
- TestStackName: The name of the stack that creates the test endpoint
- TestStackConfig: The file name for the test configuration file for the test stack’s template
- ProdStackName: The name of the stack that creates the production endpoint
- ProdStackConfig: The file name for the test configuration file for the production stack’s template
- Email: The email where CodePipeline will send SNS notifications
- GitHubToken: A Secret OAuthToken with access to the GitHub repo
- GitHubUser: GitHub Username
- Repo: The name (not URL) of the GitHub repository to pull from
- Branch: The name (not URL) of the GitHub repository’s branch to use
- SageMakerEndpointName: The name of the SageMaker Endpoint


Deployment Steps
  Step 1. Prepare an AWS Account
  Step 2. Launch the Stack
  Step 3. Test and Approve the Deployment

Summary

Additional Resources
