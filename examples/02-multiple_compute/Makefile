# Example directory names start with a digit
EXAMPLE_DIRS = $(wildcard [0-9]*/)

all:
	python3 convert.py

clean:
	for dir in $(EXAMPLE_DIRS); do                                          \
		echo;                                                               \
		echo "------- Cleaning example $$dir ----------------" ;            \
		$(MAKE) -C $$dir clean;                                             \
	done
