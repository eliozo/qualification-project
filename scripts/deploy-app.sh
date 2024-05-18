pwd
cd qualification-project
git pull origin main
pwd
cd /etc/our-flasks/eliozo
pwd
rm -fr *
pwd
cp -r /var/lib/jenkins/workspace/deploy-eliozoapp/qualification-project/eliozoapp/* .
sudo systemctl stop eliozo.service 
sudo systemctl restart nginx
sudo systemctl start eliozo.service
