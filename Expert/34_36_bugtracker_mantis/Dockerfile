# Use an official PHP image with Apache
FROM php:7.4-apache

# Install dependencies and PHP extensions required by MantisBT
RUN apt-get update && apt-get install -y \
    libpng-dev libjpeg-dev libpq-dev libzip-dev unzip curl git \
    && docker-php-ext-install gd pdo pdo_mysql pdo_pgsql zip

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Download and setup MantisBT
RUN curl -L https://github.com/mantisbt/mantisbt/archive/refs/tags/release-2.25.2.tar.gz | tar xz \
    && mv mantisbt-release-2.25.2 /var/www/html/mantisbt \
    && chown -R www-data:www-data /var/www/html/mantisbt

# Set the working directory
WORKDIR /var/www/html/mantisbt

# Install MantisBT PHP dependencies using Composer
RUN composer install --no-dev

# Expose port 80 for web access
EXPOSE 80


# docker-compose up -d --build

# Once done, just open http://localhost:8080/mantisbt