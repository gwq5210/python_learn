all: lib.so

lib.so: test_ctypes.cpp
	g++ -shared -fPIC -o $@ $<

clean:
	rm -rf lib.so
