#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static


#Install nginx if it doesn't exist

if ! command -v nginx &> /dev/null
then
    sudo apt update
    sudo apt install nginx -y
fi

#Creating needed Folders

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#Creating a Prototype html file for Testing purpose
echo "<!DOCTYPE html>
<html>
    <head>
        <title>Home - AirBnB clone</title>
    </head>
    <body>
        <h1>Welcome to AirBnB clone - Deploy static!</h1>
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#Creating Symbolic link as needed
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

#Setting the permission to user:ubuntu
sudo chown -R ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

#Restarting the Nginx
sudo service nginx restart
