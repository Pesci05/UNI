OBJ = main.o stampa.o

exec.stampa: $(OBJ)
	g++ -o exec.stampa $(OBJ)

main.o: src/main.cpp 
	g++ -c src/main.cpp

stampa.o: src/stampa.cpp 
	g++ -c src/stampa.cpp

depend:
	g++ -MM src/*.cpp > depend.mk

-include depend.mk

clean:
	rm -f *.o 

cleanall: clean
	rm -f  *.o exec.stampa

