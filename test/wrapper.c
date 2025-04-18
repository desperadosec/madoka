#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    execv(argv[1], 0);
}
