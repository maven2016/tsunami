# Tsunami Security Scanner Deployment

Public Image available: maven2016/tsunami:1.0.0 <br/>
Dockerfile included in git as well.<br/>

docker-compose deployment: <br/>
modify hosts.txt to include ipv4 addresses to scan. <br/>
modify docker-compose.yaml envrionment variables: 
  1. RECIPIENT - where to send the scan reports. 
  2. SENDER - AWS SES verified email address to send from.
  3. AWS_REGION - AWS Region where the verfied SES email address is located. </br>
Make sure to have AWS Profile with AWS SES access in ~/.aws/credentials </br>
or comment out in the volumes block: - ~/.aws:/root/.aws </br>
and add environment variables:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY

To bring up the env:
docker-compose up -d 
To destroy the env:
docker-compose down


helm3 deployment:
Enter values in values.yaml

To bring up the env:
helm upgrade --install tsunami -f values.yaml .
To destroy the env:
helm delete tsunami
