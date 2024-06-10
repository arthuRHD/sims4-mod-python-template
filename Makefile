BASE_ZIP=resources/base.zip
SRC_DIR=src
OUTPUT_DIR=output
TS4SCRIPT_NAME=MyMod.ts4script

all: package

unzip:
	@echo "Unzipping $(BASE_ZIP)..."
	unzip -o $(BASE_ZIP) -d $(OUTPUT_DIR)

compile:
	@echo "Compiling Python files in $(SRC_DIR)..."
	python -m compileall $(SRC_DIR)

package: compile
	@echo "Packaging mod into $(TS4SCRIPT_NAME)..."
	@cd $(SRC_DIR) && zip -r ../$(TS4SCRIPT_NAME) .

clean:
	@echo "Cleaning up..."
	@rm -rf $(OUTPUT_DIR)
	@rm -f $(TS4SCRIPT_NAME)
	@find $(SRC_DIR) -name '*.pyc' -delete
	@find $(SRC_DIR) -name '__pycache__' -delete

run:
	@echo "Running mod script..."
	python $(SRC_DIR)/my_mod.py

help:
	@echo "Available targets:"
	@echo "  unzip   - Unzip the base.zip file"
	@echo "  compile - Compile Python files to .pyc"
	@echo "  package - Package the mod into a .ts4script file"
	@echo "  clean   - Clean up generated files"
	@echo "  run     - Run the mod script"
	@echo "  help    - Display this help message"

.PHONY: all unzip compile package clean run help
