# Brett_Bonner_Resume

Resume: https://d1gcft6jzct941.cloudfront.net

# Background

The Cloud Resume Challenge is a hands on project designed to showcase practical cloud skills by deploying a personal resume site using AWS services. My goal was to create a live HTML/CSS resume hosted on AWS, with a serverless backed that tracks visitor counts. It also served as a great opportunity to build comfort with infrastructure as code, security policies, and CI/CD.

# Understanding

The challenge required:
    - Hosting a static resume on the internet (S3 + Cloudfront)
    - Making it secure with HTTPS
    - Adding a javascript based counter that fetches data from a backend API
    - Building that API with API Gateway + Lambda + DynamoDB
    - Connecting all the pieces while keeping the site publicly usable

# Implementation

Frontend
    - Built the resume using HTML and CSS
    - Deployed it to an S3 bucket configured for static website hosting
    - Distributed it globally with CloudFront
Visitor Counter
    - Wrote JavaScript that uses fetch() to hit an API and retrieve a visitor count.
    - Connected that request to a backend built with:
        - API Gateway: to expose an HTTPS endpoint
        - Lambda: to update and retrieve the visitor count
        - DynamoDB: to persist the counter
Infrastructure
    - Managed permissions using IAM roles
    - Gave Lambda permissions to write to DynamoDB
    - Added CORS support to the API so the frontend could make cross-origin requests
    - Used CloudWatch logs to debug errors coming from Lambda

# Lessons Learned

CORS (Cross-Origin Resource Sharing)

    One of the first road blocks I hit was dealing with CORS. I have never heard of CORS before this but have heard of the concept before this.

    What is CORS?

    CORS is a security feature built into web browsers. It's designed to prevent a webpage from making unauthorized requests to a different domain than the one it was loaded from. This policy protects users from malicious websites trying to steal data or interact with services they shouldn't have access to.

    How CORS Affected My Project?

    In this project, I built a counter using:
        Frontend: Javascript in my HTML page
        Backend: An API built with API Gateway + Lambda + DynamoDB
    When the JavaScript on my resume site tried to call the backend API to fetch the current visitor count, the browser blocked the request.

    What I Had to Do

    To fix the issue, I had to update both my API Gateway configuration and my lambda function response:
        - I went into the API Gateway console, selected the Get /visitor method, and enabled CORS
        - The actual response from my lambda function also needed to include CORS headers, specifically:
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        -This header tells the browser that any site is allowed to access this API.

    CI/CD and Github Actions

    Setting up continuous integration and deployment(CI/CD) using GitHub Actions was one of the most rewarding and challenging parts of the project.
    
    I created two automated workflows:
        1. Frontend Deployment Workflow
            - On every push to the main branch, the workflow uploaded updated resume files to an S3 bucket
            - Triggered a CloudFront cache invalidation so changes would appear immediately.
        2. Backend Deployment Workflow
            - This pipeline handled packaging and deploying my Lambda function using the AWS CLI. It ensured that any updates to my backend logic were pushed live automatically.
    
    To authenticate these workflows with AWS, I used Github Secrtes. I securely stored my keys in GitHub and referenced them in the workflows. This was also my first time working with .yml files. I learned how YAML syntax works, using indentation and key value pairs, and how GitHub Actions runners interpret those workflows in sequence.

    CI/CD Challenges

    At first, my workflows failed because I hadn't set the right IAM permissions for my AWS user. I had to revise my AWS policy to include access to lambda, S3, apigateway, and cloudfront.

    My backend deployment kept failing because of a small misconfiguration - I had incorrect file paths in the YAML file, and I was missing aws-cli installation steps in the runner environment.

# Deliverables

1. Live Resume Website 
    - HTML/CSS resume hosted on AWS S3 and served securely through CloudFront with HTTPS
2. Serverless Infrastructure
    - All backend infrastructure deployed without traditional servers, using IAM for access control, CloudWatch for logging, and DynamoDB for storage
3. CI/CD Pipelines
    - Frontend CI/CD: Deploys static site to S3
    - Backend CI/CD: packages and deploys lambda function using GitHub Actions
    - Utilized GitHub Secrets for secure AWS credential handling
