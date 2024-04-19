# questionable

[![](https://img.shields.io/badge/Version-1.0.1-green)](https://github.com/PixelSymbols/questionable) [![](https://img.shields.io/badge/Author-PixelSymbols%20purple)](https://github.com/PixelSymbols)

### A simple python package to get non-empty value out of 2 options

If both are empty, `None` will be returned.
If both have a value, first value will be returned
- [Installation](#Installation)
- [Examples](#Examples)
- [Description](#Description)
- [Author](#Author)
- [License](#License)
- [Dependencies](#Dependencies)

## Installation

```cmd
pip install questionable
```

## Examples

### how to use:

```py
import questionable as qq

def your_func(your_args=...):
	# your code
	...
	return qq(<your value>,<default value>) # `<your value>` will be returned
```

- Values can be:
	- `int`
	- `float`
	- `str`
	- `None`
	- `bool`
	- `list`
	- `tuple`
	- `set`

## Description

### Why?

instead of doing:
```py
class NotYoutubeLink(Exception):
	def __str__(self):
		text = super().__str__()
		if text: return text
		return "This link is not from youtube! :bonk:"
```
you will be able todo:
```py
import questionable as qq

class NotYoutubeLink(Exception):
	def __str__(self):
		return qq(super().__str__(),"This link is not from youtube! :bonk:")
```

### other cases

see [test.py](https://github.com/PixelSymbols/questionable/blob/main/questionable/test.py) to better understand what would happen in other cases. But in short:
both aren't empty -> first will be returned
both are empty -> None will be returned
first isn't empty -> first will be returned
second isn't empty -> second will be returned

## Author
**PixelSymbols**
- [Github](https://github.com/PixelSymbols)

## Dependencies

```
is_empty
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENCE.MD) file for details