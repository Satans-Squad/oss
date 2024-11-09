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

    // Open shared memory object
    shm_fd = shm_open(SHM_NAME, O_RDONLY, 0666);
    ptr = mmap(0, SHM_SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);

    // Read the message from shared memory
    printf("Message read from shared memory: %s\n", ptr);

    // Clean up
    munmap(ptr, SHM_SIZE);
    close(shm_fd);
    shm_unlink(SHM_NAME); // Clean up shared memory
    return 0;
}
