// THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
// A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Simon Marty.
//
#include "myar.h"
#include <stdio.h>
#include <dirent.h>
#include <fcntl.h>
#include <unistd.h>
#include <utime.h>

long getBufferSize(char *file);

int fill_ar_hdr(char *filename, struct ar_hdr *hdr) {

    struct stat statbuf;

    if(stat(filename, &statbuf) == -1) {
        perror("Failed to stat file");
        exit(EXIT_FAILURE);
    }

    int null_byte_pos = sprintf(hdr -> ar_name, "%-s", filename);
    hdr -> ar_name[null_byte_pos] = '/';
    int i;
    for(i = null_byte_pos + 1; i < 16; i++) {
        hdr -> ar_name[i] = ' ';
    }

    sprintf(hdr -> ar_date, "%-12ld", statbuf.st_mtime);
    sprintf(hdr -> ar_uid, "%-6d", statbuf.st_uid);
    sprintf(hdr -> ar_gid, "%-6d", statbuf.st_gid);
    sprintf(hdr -> ar_mode, "%-8o", statbuf.st_mode);
    sprintf(hdr -> ar_size, "%-10ld", statbuf.st_size);
    strcpy(hdr -> ar_fmag, ARFMAG);

    return 0;
}

int fill_meta(struct ar_hdr hdr, struct meta *meta) {

    sscanf(hdr.ar_name, "%[^/]s", meta -> name);
    sscanf(hdr.ar_date, "%12ld", &meta -> mtime);
    sscanf(hdr.ar_uid, "%6d", &meta -> uid);
    sscanf(hdr.ar_gid, "%6d", &meta -> gid);
    sscanf(hdr.ar_mode, "%8o", &meta -> mode);
    sscanf(hdr.ar_size, "%10d", &meta -> size);

    return 0;
}

int _q(char *arfile, char *fileToAppend) {

    int arch_fd;

    arch_fd = open(arfile, O_CREAT | O_RDWR, 0666);

    struct stat *arstat = malloc(sizeof(*arstat));

    stat(arfile, arstat);

    if(arstat -> st_size == 0) {    // Is empty file
        write(arch_fd, ARMAG, SARMAG);
    }
    else {
        char armag_checker[SARMAG];
        read(arch_fd, armag_checker, SARMAG);

        if(strcmp(armag_checker, ARMAG) != 0) {
            perror("not an archive file");
            exit(EXIT_FAILURE);
        }
    }

    lseek(arch_fd, 0, SEEK_END);

    if(fileToAppend == NULL) {
        return 0;
    }

    long buffer_size;
    int amount_read;

    buffer_size = getBufferSize(fileToAppend);
    char buffer[buffer_size];
	
	struct stat file_stat;
    stat(fileToAppend, &file_stat);

    if(S_ISREG(file_stat.st_mode) == 0) {   // file is not ordinary, not an error, just ignore
		return 0;
	}

    struct ar_hdr *hdr = malloc(sizeof(struct ar_hdr));

    fill_ar_hdr(fileToAppend, hdr);

    write(arch_fd, hdr, 60);

    int file;
    if((file = open(fileToAppend, O_RDONLY)) == -1) {
        perror("failed to read a file");
        exit(EXIT_FAILURE);
    }

    while ((amount_read=read(file, buffer, buffer_size)) > 0)
        write(arch_fd, buffer, amount_read);

    if(amount_read == -1) {
        perror("read");
        exit(EXIT_FAILURE);
    }
    write(arch_fd, "\n", 1);
    return 0;
}

long getBufferSize(char *file) {
    struct stat stat_buffer;

    if(stat(file, &stat_buffer) == -1) {
        perror("Failed to stat file");
        exit(EXIT_FAILURE);
    }

    return stat_buffer.st_blksize;
}

int _A(char *ar_path) {

    DIR *dir;

    if((dir = opendir("./")) == NULL) {
        perror("opendir");
        exit(EXIT_FAILURE);
    }

    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        char filename[NAME_MAX];
        sprintf( filename , "%s", entry->d_name) ;
        struct stat *statbuf = malloc(sizeof(*statbuf));

        if( stat(filename, statbuf) == -1) {
            perror("stat failed");
            continue;
        }

        if(S_ISDIR(statbuf -> st_mode) != 0) {
            continue;
        }

        _q(ar_path, filename);
    }

    return 0;
}

int _xo(char *archive_path, char *fileToExtract) {
	
    int archive_file_fd;
    int file_created_fd;
    struct ar_hdr *ar_hdr_buffer;
    struct meta *meta;

    if((archive_file_fd = open(archive_path, O_RDONLY)) == -1) {
        perror("failed to open archive");
        exit(EXIT_FAILURE);
    }

    char armag_checker[SARMAG];
    read(archive_file_fd, armag_checker, SARMAG);

    if(strcmp(armag_checker, ARMAG) != 0) {
        perror("not an archive file");
        exit(EXIT_FAILURE);
    }


	while(1) {
        ar_hdr_buffer = malloc(sizeof(struct ar_hdr));
        meta = malloc(sizeof(struct meta));

        read(archive_file_fd, ar_hdr_buffer, sizeof(struct ar_hdr));
        fill_meta(*ar_hdr_buffer, meta);

        if (strcmp(meta->name, fileToExtract) == 0) {

            if ((file_created_fd = open(fileToExtract, O_CREAT | O_WRONLY, meta -> mode)) == -1) {
                perror("failed to create file");
                exit(EXIT_FAILURE);
            }

            long buffer_size = getBufferSize(archive_path);
            char buffer[buffer_size];
            int  amount_read;
            int amount_left = meta -> size;

            while ((amount_read=read(archive_file_fd, buffer, buffer_size)) > 0) {

                if (amount_read > amount_left) {
                    write(file_created_fd, buffer, amount_left);
                    break;
                } else {
                    write(file_created_fd, buffer, amount_read);
                }
                amount_left -= amount_read;
            }

            if(amount_read == -1) {
                perror("read");
                exit(EXIT_FAILURE);
            }

            struct utimbuf time;
            time.actime = meta -> mtime;
            time.modtime = meta -> mtime;
            utime(fileToExtract, &time);

            exit(EXIT_SUCCESS);
        }
        else {
            lseek(archive_file_fd, meta -> size, SEEK_CUR);
        }
    }

}


int _t(char *ar_filepath) {
    int ar_fd;

    if((ar_fd = open(ar_filepath, O_RDONLY)) == -1) {
        perror("failed to open archive");
        exit(EXIT_FAILURE);
    }

    char armag_checker[SARMAG];
    read(ar_fd, armag_checker, SARMAG);

    if(strcmp(armag_checker, ARMAG) != 0) {
        perror("not an archive file");
        exit(EXIT_FAILURE);
    }

    struct stat *statbuf = malloc(sizeof(*statbuf));

    if((stat(ar_filepath, statbuf)) == -1) {
        perror("Could not stat archive");
        exit(EXIT_FAILURE);
    }

    while(1) {
        struct ar_hdr *hdr = malloc(sizeof(struct ar_hdr));
        struct meta *meta = malloc(sizeof(struct meta));

        read(ar_fd, hdr, 60);
        fill_meta(*hdr, meta);

        printf("%s\n", meta -> name);

        if(lseek(ar_fd, meta -> size + 1, SEEK_CUR) >= statbuf->st_size) {
            exit(EXIT_SUCCESS);
        }
    }
}

int main(int argc, char **argv) {
    if(argc < 3) {
        print_info();
        return 0;
    }

    char *key = argv[1];
    char *afile = argv[2];

    if(strcmp(key, "q") == 0) {
        if(argc <= 2) {
            print_info();
            return 0;
        }
        else if(argc == 3) {
            _q(afile, NULL);
        }
        else {
            // Not super efficient, many writes.
            int i;
            for (i = 3; i < argc; i++)
                _q(afile, argv[i]);
        }
    }
    else if(strcmp(key, "xo") == 0) {
        if(argc < 3) {
            print_info();
            return 0;
        }
        int i;
        for(i = 3; i < argc; i++)
            _xo(afile, argv[i]);
    }
    else if(strcmp(key, "t") == 0) {
        _t(afile);
    }
    else if(strcmp(key, "A") == 0) {
        _A(afile);
    }
    else {
        print_info();
    }
    return 0;
}

int print_info() {
    printf("Usage: myar archive-file file...\n");
    printf(" commands:\n");
    printf("  q\t\t  - quickly append named files to archive\n");
    printf("  xo\t\t  - extract named files with metadata\n");
    printf("  t\t\t  - display contents of the archive\n");
    printf("  d\t\t  - delete named files from archive\n");
    printf("  A\t\t  - quickly append all \"regular\" files "
           "in the current directory (except the archive itself)\n");
    return 0;
}

