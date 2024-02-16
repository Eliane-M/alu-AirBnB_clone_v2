#!/usr/bin/env bash
# Sets up the servers for deployment of the web_static


#installing nginx if its not already installed
sudo apt-get update
sudo apt-get install -y nginx

#creating the folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#create fake HTML file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"|sudo tee /data/web_static/releases/test/index.html

# for the symbolic link
sudo ln -fs /data/web_static/releases/test/  /data/web_static/current

# giving ownership to the /data/ folder
sudo chown -R ubuntu:ubuntu /data/

# updating nginx configuration
nginx_config="server {
    listen 80;
    listen [::]:80;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}"

echo "$nginx_config" | sudo tee /etc/nginx/sites-available/default > /dev/null
sudo service nginx restart
