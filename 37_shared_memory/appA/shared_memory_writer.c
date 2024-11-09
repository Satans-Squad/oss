#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>

#define SHM_NAME "/my_shm"
#define SHM_SIZE 256

int main() {
    int shm_fd;
    char *ptr;

    // Create shared memory object
    shm_fd = shm_open(SHM_NAME, O_CREAT | O_RDWR, 0666);
    ftruncate(shm_fd, SHM_SIZE);
    ptr = mmap(0, SHM_SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);

    // Write a message to shared memory
    const char *message = "Hello from App A!";
    sprintf(ptr, "%s", message);
    printf("Message written to shared memory: %s\n", message);

    // Clean up
    munmap(ptr, SHM_SIZE);
    close(shm_fd);
    return 0;
}
