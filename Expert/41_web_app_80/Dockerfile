FROM php:8.0-apache

# Install PDO MySQL extension
RUN docker-php-ext-install pdo pdo_mysql

# Enable Apache modules
RUN a2enmod rewrite
RUN a2enmod headers

# Copy Apache configuration
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

# Copy application files
COPY . /var/www/html/

# Set correct permissions
RUN chown -R www-data:www-data /var/www/html/ \
    && chmod -R 755 /var/www/html/ \
    && chmod 644 /var/www/html/*.php

# Set environment variables
ENV DB_HOST=mysql-db
ENV DB_NAME=logindb
ENV DB_USER=root
ENV DB_PASSWORD=rootpassword

# Expose port 80
EXPOSE 80

# Restart Apache
CMD ["apache2-foreground"]