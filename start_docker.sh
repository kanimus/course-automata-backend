# setup config.py file
yes | cp -i src/config/settings/config.template.py src/config/settings/config.py
# create folder for db
mkdir -p pgdata
# start docker-compose
UID_GID="$(id -u):$(id -g)" docker-compose up --build -d