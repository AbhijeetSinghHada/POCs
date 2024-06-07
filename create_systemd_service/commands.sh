cd /etc/systemd/system/

# create a file with .service extension and paste contents to it

# paste then file contents
sudo systemctl daemon-reload
sudo systemctl start test
sudo systemctl status test

# for adding that to startup
sudo systemctl enable test