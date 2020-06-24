#!/usr/bin/env bash

NGINX_CONF_FILE="nginx.conf"
NGINX_CONF_DEST="/etc/nginx/nginx.conf"
NGINX_CONTAINER="some-nginx"
APACHE_CONF_FILE="apache.conf"
APACHE_CONF_DEST="/usr/local/apache2/conf/httpd.conf"
APACHE_CONTAINER="my-apache-app"

help()
{
    echo "Tool for installing the generated configuration file in the specified server."
    echo
    echo "Syntax: conf-server.sh [nginx|apache]"
}

conf_nginx()
{
    if docker cp ${NGINX_CONF_FILE} ${NGINX_CONTAINER}:${NGINX_CONF_DEST}; then
        echo -e "\e[32mWritten configuration to Nginx container."
    else
        echo -e "\e[91mError while writing configuration to Nginx container."
        return 1
    fi
}

conf_apache()
{
    echo -e "\e[91mWork in progress, not really working..."
    if docker cp ${APACHE_CONF_FILE} ${APACHE_CONTAINER}:${APACHE_CONF_DEST}; then
        echo -e "\e[32mWritten configuration to Apache container."
    else
        echo -e "\e[91mError while writing configuration to Apache container."
        return 1
    fi
}

if [[ $# -gt 0 ]]
then
    server="$1"

    case $server in
        "nginx")
        conf_nginx
        ;;
        "apache")
        conf_apache
        ;;
        *)
        help
        ;;
    esac
else
    help
fi
