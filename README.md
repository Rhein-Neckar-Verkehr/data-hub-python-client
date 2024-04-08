# RNV Open Data Client 
A simple client in python to access the RNV Open Data API.

This readme file contains information about using the client. For detailed documentation on how to use the GraphQL interface, see the documentation [link from here](https://www.opendata-oepnv.de/ht/de/organisation/verkehrsunternehmen/rnv/openrnv/data-hub-api-dokumentationen)

# How to use

Go to the folder python in this directory, and install requirements. In example: 
```bash 
    $ cd python
    $ pip install requirements.txt 
``` 
Run python script: 
```bash 
    $ python3 run_open_data_request.py 
```


# Preparation steps 
## Obtain Credentials 
To get access to our Open Data Hub API with your solutions, it is necessary to have an oauth2 access token. 
You need to go through several steps to generate such a token 


1. You register with your name and email for "Graphql" access with the reason "Upper Hackathon 24" here. 
[Open RNV Formular](https://www.opendata-oepnv.de/ht/de/organisation/verkehrsunternehmen/rnv/openrnv/api)
2. In around 10 minutes you should receive a mail with your basic credentials, it's recommended to save the mail 
3. From these credentials you can generate an access token for your coded clients, there are several ways to obtain such a token,
some of them are described here. 

## Prepare credentials

1. Download the graphql.http file to this repo and place it in the root path. 
2. Download the preparation script from gist (see below)
3. Run the shell script ./prepare_env_file.sh this will generate a .env file which is read by the application

### On Unix/Mac/Linux 

```bash 
$ curl https://gist.githubusercontent.com/rnv-opendata/8365b1317505a80359491c2124a05e94/raw/2fc73bdbb1dd4872feff7aa8182c477d01a379cc/prepare_env_file.sh > prepare_env_file.sh
$ sudo chmod u+rwx prepare_env_file.sh 
$ ./prepare_env_file.sh > .envs
```
### On Windows 
```bash 
$ curl https://gist.githubusercontent.com/rnv-opendata/900d43affca063caed7918f91d9531b5/raw/38060421063bc4766566e5324af489fbce226cac/prepare_env_file.cmd > prepare_env_file.cmd  
$ pwsh prepare_env_file.cmd
```

## Packaging 
Wheels for usage as package can be built like this. 

```bash
python setup.py sdist bdist_wheel
```


# Important Links 
1. [RNV Data-Hub-API Main Page and Credentials Request](https://www.opendata-oepnv.de/ht/de/organisation/verkehrsunternehmen/rnv/openrnv/api)
2. [RNV Opendata GitHub Repository](https://github.com/Rhein-Neckar-Verkehr/data-hub-nodejs-client)
