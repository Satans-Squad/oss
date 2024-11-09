Follow this article steps in case you are not able to do it with the above mentioned steps
https://medium.com/@1993Tikku/deploying-mediawiki-mysql-using-docker-32a0626550f7

1. run 
    docker-compose up -d

2. go to localhost:8080 and continue to setup the wiki first
3. run 
    docker ps 

    docker inspect mysql_db

    find the ip address of the container which is at the bottom of the page (make sure not to be confused with the gatway ip*)

4. enter the above information in the host field
    your_mysql_container_ip:3306

5. enter "wiki_db" at both db name and prefix field

6. enter "root" as user and password

7. continue till the end

8. Now LocalSettings.php will be downloaded so run the above command

9. go to Downloads

10. run

    docker cp ./LocalSettings.php LAMP:/var/www/html

11. go to localhost:8080 and now you'll see the landing page

