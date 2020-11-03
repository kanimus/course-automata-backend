# setup config.py file
yes | cp -i src/config/settings/config.template.py src/config/settings/config.py
# create folder for db
mkdir -p pgdata
# start docker-compose
docker-compose -f docker-compose.yaml up -d