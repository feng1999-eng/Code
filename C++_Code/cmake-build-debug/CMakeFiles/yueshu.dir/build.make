# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.15

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

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "D:\clion\CLion 2019.3.4\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "D:\clion\CLion 2019.3.4\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\Code\C++_Code

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\Code\C++_Code\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/yueshu.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/yueshu.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/yueshu.dir/flags.make

CMakeFiles/yueshu.dir/shulun/yueshu.cpp.obj: CMakeFiles/yueshu.dir/flags.make
CMakeFiles/yueshu.dir/shulun/yueshu.cpp.obj: ../shulun/yueshu.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Code\C++_Code\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/yueshu.dir/shulun/yueshu.cpp.obj"
	D:\PROGRA~3\MINGW-~1\X86_64~1.0-W\mingw64\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\yueshu.dir\shulun\yueshu.cpp.obj -c D:\Code\C++_Code\shulun\yueshu.cpp

CMakeFiles/yueshu.dir/shulun/yueshu.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/yueshu.dir/shulun/yueshu.cpp.i"
	D:\PROGRA~3\MINGW-~1\X86_64~1.0-W\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E D:\Code\C++_Code\shulun\yueshu.cpp > CMakeFiles\yueshu.dir\shulun\yueshu.cpp.i

CMakeFiles/yueshu.dir/shulun/yueshu.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/yueshu.dir/shulun/yueshu.cpp.s"
	D:\PROGRA~3\MINGW-~1\X86_64~1.0-W\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S D:\Code\C++_Code\shulun\yueshu.cpp -o CMakeFiles\yueshu.dir\shulun\yueshu.cpp.s

# Object files for target yueshu
yueshu_OBJECTS = \
"CMakeFiles/yueshu.dir/shulun/yueshu.cpp.obj"

# External object files for target yueshu
yueshu_EXTERNAL_OBJECTS =

yueshu.exe: CMakeFiles/yueshu.dir/shulun/yueshu.cpp.obj
yueshu.exe: CMakeFiles/yueshu.dir/build.make
yueshu.exe: CMakeFiles/yueshu.dir/linklibs.rsp
yueshu.exe: CMakeFiles/yueshu.dir/objects1.rsp
yueshu.exe: CMakeFiles/yueshu.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Code\C++_Code\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable yueshu.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\yueshu.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/yueshu.dir/build: yueshu.exe

.PHONY : CMakeFiles/yueshu.dir/build

CMakeFiles/yueshu.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\yueshu.dir\cmake_clean.cmake
.PHONY : CMakeFiles/yueshu.dir/clean

CMakeFiles/yueshu.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Code\C++_Code D:\Code\C++_Code D:\Code\C++_Code\cmake-build-debug D:\Code\C++_Code\cmake-build-debug D:\Code\C++_Code\cmake-build-debug\CMakeFiles\yueshu.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/yueshu.dir/depend
