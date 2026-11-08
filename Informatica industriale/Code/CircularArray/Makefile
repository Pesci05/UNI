CC=gcc
CFLAGS=-Wall -pthread
LDFLAGS=-lpthread

all: main.exe

main.exe: CircularArray.o main.o
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

CircularArray.o: CircularArray.c CircularArray.h
	$(CC) $(CFLAGS) -c $< -o $@

main.o: main.c CircularArray.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	del *.o main

