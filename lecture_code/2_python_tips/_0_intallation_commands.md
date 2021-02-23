# Installation Instructions
## Installing Python
Go to: https://www.python.org/downloads/

I suggest adding Python to your PATH variable

## Setting a Virtual Environment
Most Python projects rely on using a number of third-party packages/modules.
When working on a number of projects, it's a good practice to have an isolated environment for each project
to avoid installation conflicts and minimize complications.

To set up a Virtual Environment, navigate to folder of you choosing, <venv_folder>, then excute command:

`> python -m venv <venv_name>`

To activate virtual environment on Windows, in <venv_folder> run:

`> .\beluga_course_test\Scripts\activate`

Now `python` and `pip` commands point to Python interpreter in the folder <venv_folder>\<venv_name>

## Installing packages

To install a package from PyPI:

`> pip install <package_name>`

Multiple packages may be installed at once:

`> pip install <package_name_1> <package_name_2> <package_name_3>`

If permission error occurs, try installing for your user account only (not applicable to virtual environments):

`> pip install <package_name> --user`

Installing from a local folder that is editable:

`> pip install -e <folder_address>`

## Installing beluga

Navigate to folder where you want beluga installed, and clone the latest version from GitHub:

`> git clone https://github.com/Rapid-Design-of-Systems-Laboratory/beluga`

Navigate into beluga folder (where `setup.py`) exists, and install beluga:

`pip install -e .[dev]`





