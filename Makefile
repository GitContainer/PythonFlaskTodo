.PHONY: docs test

help:
	@echo "  env         create a development environment using virtualenv"
	@echo "  deps        install dependencies using pip"
	@echo "  clean       remove unwanted files like .pyc's"
	
env:
	# sudo pacman -S python-pip
	# sudo pacman -S python-virtualenv 
	pyvenv env && \
	. env/bin/activate && \
	make deps

deps:
	pip3 install -r requirements.txt

clean:
	python3 manage.py clean
