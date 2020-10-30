FROM nginx:1.19.0-alpine
RUN mkdir /ssl
RUN rm /etc/nginx/conf.d/default.conf
# COPY nginx.conf /etc/nginx/conf.d
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
# COPY /ssl /etc/nginx/
