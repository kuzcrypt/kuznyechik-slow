all:

install:
	install -m 0644 kuznyechik_slow.py /usr/lib/python3/dist-packages

uninstall:
	rm -f /usr/lib/python3/dist-packages/kuznyechik_slow.py

clean:
	rm -rf __pycache__
