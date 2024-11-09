
1. docker build -t ubuntu-ftp-telnet .

2. docker run -d \
  --network host \
  --name ftp-telnet-server \
  ubuntu-ftp-telnet


####### FTP

1. to add the file

    docker exec -it your_container_id /bin/bash

    go to /var/ftp/pub

    run

    echo "it is working" > hello.txt

2. now from other terminal
    run

    ftp localhost

    username:anonymous
    password:any@gmail.com

3. go to pub and see the file