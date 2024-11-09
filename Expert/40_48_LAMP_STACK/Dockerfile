# Use a base image with Apache and PHP
FROM php:8.2-apache

# Install MySQL client libraries and mysqli extension
RUN apt-get update && apt-get install -y default-libmysqlclient-dev && docker-php-ext-install mysqli

# Enable mod_rewrite for Apache
RUN a2enmod rewrite

# Copy the HTML files into the container
COPY html/ /var/www/html/

# Expose port 80
EXPOSE 80
