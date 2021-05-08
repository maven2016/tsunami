import os
import glob
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = os.environ['SENDER']

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.
RECIPIENT = os.environ['RECIPIENT']

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the 
# ConfigurationSetName=CONFIGURATION_SET argument below.
#CONFIGURATION_SET = "ConfigSet"

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = os.environ['AWS_REGION']

# The subject line for the email.
SUBJECT = "tsunami scan"

# The full path to the file that will be attached to the email.
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
print(glob.glob('logs/*.json'))
ATTACHMENT = glob.glob('logs/*.json')

# The email body for recipients with non-HTML email clients.
BODY_TEXT = "Tsunami scan is complete,\r\nPlease see the attached reports."

# The HTML body of the email.
BODY_HTML = """\
<html>
<head></head>
<body>
<h1>Tsunami scan is complete</h1>
<p>Please see the attached reports.</p>
</body>
</html>
"""

# The character encoding for the email.
CHARSET = "utf-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)

# Create a multipart/mixed parent container.
msg = MIMEMultipart('mixed')
# Add subject, from and to lines.
msg['Subject'] = SUBJECT 
msg['From'] = SENDER 
msg['To'] = RECIPIENT

# Create a multipart/alternative child container.
msg_body = MIMEMultipart('alternative')

# Encode the text and HTML content and set the character encoding. This step is
# necessary if you're sending a message with characters outside the ASCII range.
textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)

# Add the text and HTML parts to the child container.
msg_body.attach(textpart)
msg_body.attach(htmlpart)

# Define the attachment part and encode it using MIMEApplication.
for f in ATTACHMENT:
    #print(f)
    with open(f, "rb") as fil:
        basename = os.path.basename(f)
        attachedfile = MIMEApplication(fil.read(), Name = basename)
        attachedfile.add_header('content-disposition', 'attachment', filename=os.path.basename(f) )
    msg.attach(attachedfile)     
#att = MIMEApplication(open(ATTACHMENT, 'rb').read())

# Add a header to tell the email client to treat this part as an attachment,
# and to give the attachment a name.
#att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))

# Attach the multipart/alternative child container to the multipart/mixed
# parent container.
msg.attach(msg_body)

# Add the attachment to the parent container.
#msg.attach(att)
#print(msg)
try:
    #Provide the contents of the email.
    response = client.send_raw_email(
        Source=SENDER,
        Destinations=[
            RECIPIENT
        ],
        RawMessage={
            'Data':msg.as_string(),
        },
        #ConfigurationSetName=CONFIGURATION_SET
    )
# Display an error if something goes wrong. 
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])
