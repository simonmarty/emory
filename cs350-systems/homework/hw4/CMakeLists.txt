cmake_minimum_required(VERSION 3.15)
project(hw4 C)

set(CMAKE_C_STANDARD 11)

add_executable(manage defs.h manage.c)
add_executable(report defs.h report.c)
add_executable(compute defs.h compute.c)