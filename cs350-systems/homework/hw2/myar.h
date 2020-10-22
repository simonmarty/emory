//
// Created by smarty on 2019-10-21.
//

#ifndef HW2_MYAR_H
#define HW2_MYAR_H

#include <stdlib.h>
#include <string.h>
#include <ar.h>
#include <sys/stat.h>

struct meta {
    char name[16];
    int mode;
    int size;
    int uid;
    int gid;
    time_t mtime;
};

int fill_ar_hdr(char *filename, struct ar_hdr *hdr);

int fill_meta(struct ar_hdr hdr, struct meta *meta);

int _q(char *arfile, char *fileToAppend);

int _xo();

int _t();

int _A();

int print_info();

#endif //HW2_MYAR_H
