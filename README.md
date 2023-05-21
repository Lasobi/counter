# Counter
This is a simple GUI application built with Python and Tkinter. It allows for the creation of multiple counters with command line arguments. You can increment and decrement the counters with '+' and '-' buttons respectively.

## Installation
To install the necessary dependencies, simply use pip:

    pip install -r requirements.txt

## Usage
To start the application, use the following command:

    python counter.py -c 1 2 3 Counter1 Counter2 Counter3

The above command will create three counters named "Counter1", "Counter2", and "Counter3", each with the initial counts of 1, 2, and 3 respectively.

You can use the following options:

* "names": A list of names for the counters.
* "-c, --count": The initial count value(s) for the counters.

## Packaging with PyInstaller
To package the application into a standalone executable with PyInstaller, first install PyInstaller with pip:

    pip install pyinstaller

Then, you can package the application with:

    pyinstaller --onefile counter.py

The standalone executable will be located in the "dist" directory.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)