# Coursehelper back #

## How to run prod ##
1) Go to work directory.
2) Run `sh run.prod.sh`
---
## How to run dev ##
1) Go to work directory.
2) Put ssl certificates to `data/certbot/conf/live/$host_domain/`
3) Edit nginx config for dev.
4) Run `sh run.dev.sh`
---
## How to run local ##
1) Go to work directory.
2) Edit and copy `src/config/settings/config.template.py` to `src/config/settings.config.py`
3) Run `docker-compose -f docker-compose.local.yaml up -d` 