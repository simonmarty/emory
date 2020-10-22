
#include <sys/types.h> /* for creat */
#include <sys/stat.h>
#include <fcntl.h>

#include <stdlib.h> /* for exit */

#include <unistd.h> /* for close */


#include <stdio.h> /* for perror*/
#include <errno.h>

int main() {

	int fd;
	if ((fd=creat("abc",0))== -1) {
		perror("creat");
		exit (1);
		}
	close(fd);
}
