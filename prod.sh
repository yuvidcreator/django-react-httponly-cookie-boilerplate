#! /bin/bash
set -e

# git pull origin main
# Attention: Replace YOUR_DOMAIN with registered domain name only, exlcuding .com / .co / .in etc.

# Activate the virtualenv for this project
source ../YOUR_DOMAIN_env/bin/activate

pip install -r requirements.txt
# sudo mkdir -pv /var/log/venya/
sudo mkdir -pv ./staticfiles
sudo mkdir -pv /var/www/YOUR_DOMAIN/staticfiles
sudo mkdir -pv ./YOUR_DOMAIN/react_build

cd ./client
yarn install
yarn global add serve
yarn build
sudo cp -r ./build /var/www/YOUR_DOMAIN/react_build
cd ..

sudo chown -cR $USER:$USER /var/www/YOUR_DOMAIN
sudo chown -cR $USER:$USER /var/www/YOUR_DOMAIN/react_build
sudo chown -cR $USER:$USER /var/www/YOUR_DOMAIN/staticfiles
sudo chown -cR $USER:$USER /var/www/YOUR_DOMAIN/mediafiles
sudo chown -cR $USER:$USER .
sudo chown -cR $USER:$USER .*

# Start gunicorn going
python manage.py collectstatic --noinput
# python3 manage.py makemigrations --noinput
# python3 manage.py migrate --noinput

sudo service supervisor restart
sudo service nginx restart

