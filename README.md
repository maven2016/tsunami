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
and add environment variables: </br>
AWS_ACCESS_KEY_ID </br>
AWS_SECRET_ACCESS_KEY </br>

To bring up the env: <br>
docker-compose up -d </br>
To destroy the env: </br>
docker-compose down </br>
</br>
</br>
helm3 deployment:</br>
Enter values in values.yaml</br>
Modfiy list of hosts to scan in helm/templates/hosts.yaml
</br>
To bring up the env:</br>
helm upgrade --install tsunami -f values.yaml . </br>
To destroy the env:</br>
helm delete tsunami
