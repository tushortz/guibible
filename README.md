# GuiBible

This is a simple bible application that parses bible verses and either prints it to the console window or displays it graphically **(Pygame needed in this case)**.


## Requirements
* Python 3
* Pygame (For graphical display)


**To install pygame, use:** 

```python
	pip install pygame
```

## Installation

### *PIP*
If you have **Pip** installed, go to the `terminal window` and type:

```python
	pip install guibible
```

### `Manually`

Go to the [Python Packaging Index](https://pypi.python.org) website. Search for [guibible](https://pypi.python.org/pypi/guibible) and either download the *compressed version* for your operating system and copy it into the `Lib` --> `site-packages` directory of your `python 3`.

You can also download and run the `.msi` or `.exe` file for windows.


## Usage Instructions

### Importing

```python
	from guibible.net import Bible   # or 
    import guibible.net
```

### Usage

**All are Optional arguments**

`instance_variable = Bible(book, chapter, verse_begin, verse_end)`

> If you imported it the first way, you would have to use it this way. 
>   
>    `Default is Bible(Genesis, 1) which shows Genesis 1`
>
>   ```python
>        sample= Bible("John", 3, 16, 18) # Will get John 3:16-18
>    ```
>
>    Otherwise use:
>
>    ```python
>        sample = guibible.net.Bible("John", 3, 16)
>    ```

**To display(print) verse in console window, use:**

* `No arguments` --> sample.read() 

**To display verse in graphical format, use:**

* *No arguments* --> `sample.display()` will use the default foreground color (black) on the default background color (white).

* *One argument* --> `sample.display((0,0,255))` will use the `first argument(supplied foreground color)` on the default background color (white).
    
* *Two arguments* --> `sample.display((0,0,255), (255, 255, 0))` will use the `first argument(supplied foreground color)` on the second argument (supplied background color).

 
> See [documentation](http://www.pythonhosted.org/guibible) for full information

### Quitting

You can quit the pygame graphical window by either pressing the `Q`, `SPACE` or `ESC` key on the keyboard.

## Contribution

If you would like to contribute to this project, feel free to `fork me` on [Github](https://github.com/tushortz/guibible)


## License

MIT © 2015 Taiwo Kareem | taiwo.kareem36@gmail.com

This is free software. It is licensed under the MIT License. Feel free to use this in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and it would be great if you distribute your work under this or a similar license, but it's not required.

## Acknowledgements
 
All glory belongs to God for his mercy and guidance.


