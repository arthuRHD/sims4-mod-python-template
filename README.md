# sims4-mod-python-template

This repository contains a development environment for creating Sims 4 mods using Python 3.3.5.

It's supposed to be used inside a GitHub Codespace or locally with the Devcontainer extension of the editor of your choice.

## Usage

- **Unzip the base game script archive**:

    ```sh
    make unzip
    ```

- **Compile Python files**:

    ```sh
    make compile
    ```

- **Package the mod into a `.ts4script` file**:

    ```sh
    make package
    ```

- **Clean up generated files**:

    ```sh
    make clean
    ```

- **Run the mod script**:

    ```sh
    make run
    ```

- **Display help message**:

    ```sh
    make help
    ```

## Project Structure

- `.devcontainer/`: Contains the devcontainer configuration files.
- `src/`: Contains the Python scripts for the mod.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `Makefile`: Provides automation for common tasks.
- `README.md`: Provides information about the project.
