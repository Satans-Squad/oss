
1. docker build -t ftp-server .

2. docker run -d \
  --name ftp-container \
  -p 21:21 \
  -p 40000-40100:40000-40100 \
  --net=host \
  ftp-server


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