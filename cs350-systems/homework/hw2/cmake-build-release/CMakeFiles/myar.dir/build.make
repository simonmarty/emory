# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/smarty/clion/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/smarty/clion/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/smarty/Documents/cs350/cs350/homework/hw2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/smarty/Documents/cs350/cs350/homework/hw2/cmake-build-release

# Include any dependencies generated for this target.
include CMakeFiles/myar.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/myar.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/myar.dir/flags.make

CMakeFiles/myar.dir/myar.c.o: CMakeFiles/myar.dir/flags.make
CMakeFiles/myar.dir/myar.c.o: ../myar.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/smarty/Documents/cs350/cs350/homework/hw2/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/myar.dir/myar.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/myar.dir/myar.c.o   -c /home/smarty/Documents/cs350/cs350/homework/hw2/myar.c

CMakeFiles/myar.dir/myar.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/myar.dir/myar.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/smarty/Documents/cs350/cs350/homework/hw2/myar.c > CMakeFiles/myar.dir/myar.c.i

CMakeFiles/myar.dir/myar.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/myar.dir/myar.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/smarty/Documents/cs350/cs350/homework/hw2/myar.c -o CMakeFiles/myar.dir/myar.c.s

# Object files for target myar
myar_OBJECTS = \
"CMakeFiles/myar.dir/myar.c.o"

# External object files for target myar
myar_EXTERNAL_OBJECTS =

myar: CMakeFiles/myar.dir/myar.c.o
myar: CMakeFiles/myar.dir/build.make
myar: CMakeFiles/myar.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/smarty/Documents/cs350/cs350/homework/hw2/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable myar"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/myar.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/myar.dir/build: myar

.PHONY : CMakeFiles/myar.dir/build

CMakeFiles/myar.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/myar.dir/cmake_clean.cmake
.PHONY : CMakeFiles/myar.dir/clean

CMakeFiles/myar.dir/depend:
	cd /home/smarty/Documents/cs350/cs350/homework/hw2/cmake-build-release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/smarty/Documents/cs350/cs350/homework/hw2 /home/smarty/Documents/cs350/cs350/homework/hw2 /home/smarty/Documents/cs350/cs350/homework/hw2/cmake-build-release /home/smarty/Documents/cs350/cs350/homework/hw2/cmake-build-release /home/smarty/Documents/cs350/cs350/homework/hw2/cmake-build-release/CMakeFiles/myar.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/myar.dir/depend
