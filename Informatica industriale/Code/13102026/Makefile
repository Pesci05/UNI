#OBJ = main.o stampa.o

#exec.stampa: $(OBJ)
#	g++ -o exec.stampa $(OBJ)

#main.o: src/main.cpp 
#	g++ -c src/main.cpp

#stampa.o: src/stampa.cpp 
#	g++ -c src/stampa.cpp

#depend:
#	g++ -MM src/*.cpp > depend.mk

#-include depend.mk

#clean:
#	rm -f *.o 

#cleanall: clean
#	rm -f  *.o exec.stampa

OBJ = main.o stampa.o

# Il primo target viene eseguito digitando solo "make" o "mingw32-make"
all: exec_stampa.exe

exec_stampa.exe: $(OBJ)
	g++ -o exec_stampa.exe $(OBJ)

main.o: src/main.cpp 
	g++ -c src/main.cpp

stampa.o: src/stampa.cpp 
	g++ -c src/stampa.cpp

depend:
	g++ -MM src/*.cpp > depend.mk

-include depend.mk

# Comandi di pulizia ottimizzati per PowerShell / Windows Terminal
clean:
	@if exist *.o del /q /f *.o

cleanall: clean
	@if exist exec_stampa.exe del /q /f exec_stampa.exe

