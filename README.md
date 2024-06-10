# sims4-mod-python-template

This repository contains a development environment for creating Sims 4 mods using Python 3.3.5.

## Getting Started

To get started with this development environment:

1. Clone the repository:

    ```sh
    git clone https://github.com/arthuRHD/sims4-mod-python-template.git
    cd sims4-mod-python-template
    ```

2. Open the project in Visual Studio Code:

    - Open Visual Studio Code.
    - Use the Command Palette (`Ctrl+Shift+P`) and select `Remote-Containers: Open Folder in Container...`.
    - Choose the `sims4-mod-python-template` folder.

3. Visual Studio Code will build and open the development container with the environment set up for Sims 4 mod development.

## Using the Makefile

The `Makefile` provides several commands to automate common tasks:

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
