

install:
	sudo apt-get install python-pip
	git clone https://github.com/leapcode/pysqlcipher
	cd pysqlcipher && 	python setup.py install --bundled
	sudo pip install -r requirements.txt

run:
	python ui.py
