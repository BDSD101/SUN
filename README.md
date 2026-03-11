# Sun Safety Dashboard
Slip Slop Slap - UV and temperature tracking in melbourne.

To run this webpage using AWS stack two main functions were occupdied.
the two functions: UV-lambdas & UV-only
The database was populated to the AWS RDS enviromen and is hosted in the cloud
The file to populate the database exists in backend directory.

the funcitons have policies protecting VPC and permission changes, if changes
wanted to be done to the server and the hosting, please contact me.

the front end is hosted in a AWS bucket + S3 for the front end. You can test locally and funcionallity
can be tested using the API URL provided in the Whatsapp file.

Once done i can push deploy it properly.

A mock quick front end has been provided for reference with how the APIs should be integrated. API calls should work if hosted locally still


additinally documentation is available for database but limited on main.
Got tired.


For packages and proper running locally youve got to:

1) install all the following packages with
:
pip install fastapi mangum pymysql httpx python-dotenv openpyxl

2) for uv only:
pip install fastapi mangum httpx
3) for local dev:
pip install fastapi mangum httpx


please make sure to also have packages be compatible for linux. Meaning packages should look like:

pip install \
  --platform manylinux2014_x86_64 \
  --target . \
  --implementation cp \
  --python-version 3.12 \
  --only-binary=:all: \
  fastapi mangum pymysql httpx python-dotenv

This ensures packages are compiled for Linux (Lambda's OS) not your local Mac/Windows machine.


DO NOT ERASE __innit__.py is left empty for a reason.

when testing if the new front end works, please see the mock_index.html
will need to be reamed index.html for testing.


ive also used the following tech if you guys want to do research;

RDS -> mysql
Lamda -> python 3.12 ****
API -> gateways
S3 -> frontend hosting
cloud front -> for HTTPS hosting.
