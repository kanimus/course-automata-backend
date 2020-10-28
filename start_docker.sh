# setup config.py file
cp src/config/settings/config.template.py src/config/settings/config.py
# create folder for db
mkdir pgdata
# start docker-compose
UID_GID="$(id -u):$(id -g)" docker-compose up --build -d