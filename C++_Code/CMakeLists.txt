cmake_minimum_required(VERSION 3.15)
project(C___Code)

set(CMAKE_CXX_STANDARD 14)

add_executable(main main.cpp)
add_executable(test test.cpp)
add_executable(2020 find_near.cpp)
add_executable(2018 2018_1.cpp)
add_executable(prime shulun/prime.cpp)
add_executable(yueshu shulun/yueshu.cpp)