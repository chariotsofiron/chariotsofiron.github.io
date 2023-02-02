+++
title = "Programming Python pedantically"
slug = "python-linting"
date = 2023-01-08

[taxonomies]
tags = ["programming"]
+++

I like to adhere to a strict styleguide when programming in Python. These are some the tools I use:

- [black](https://github.com/psf/black) for code opinionated formatting
- [isort](https://github.com/PyCQA/isort) for sorting imports
- [pylint](https://github.com/PyCQA/pylint) for necessary and opinionated lints
- [mypy](https://github.com/python/mypy) for type checking
- [bandit](https://github.com/PyCQA/bandit) for security lints
- [refurb](https://github.com/dosisod/refurb) for refurbishing and modernizing Python codebases

# Why?



An initial reaction might be that doing so completely defeats the purpose of Python, and fair enough!

When I was using Python for university, it was the perfect language for implementing algorithms and completing assignments. It allowed me to focus on learning computer science instead of the details of a specific programming language.

After I graduated and was using Python for my job, I ran into issues when trying to productionize it. The lack of static-typing and compile-time checking led to a lot of runtime errors that wouldn't have ocurred in other languages. Using strict linters enable me to

- Write more legibly and idiomatically
- Find bugs in code earlier
- Design better classes and interfaces
- Write code that appears consistent across projects and team members
- Reduce time in code reviews
- Document my code better


# My `pyproject.toml`

As of somewhat recently, all of the tools mentioned above have the ability to be configured by a common `pyproject.toml` file.

<script src="https://emgithub.com/embed.js?target=https://github.com/benburk/dotfiles/blob/master/python/pyproject.toml&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>


# Black

> Black is a PEP 8 compliant opinionated formatter. Black reformats entire files in place. Style configuration options are deliberately limited and rarely added.

By default, black won't reflow this code to be on one line

```python
def foo(
    arg1,
    arg2,
)
```

Enabling `skip_magic_trailing_comma`. I'm also happy with the default line length of 88, which allows me to have two source files side by side on a 14" display.

Formatting can be for a section of code using the `fmt` directive:

```python
# fmt: off
np.array(
    [
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1],
    ]
)
# fmt: on
```

# isort

> isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.

Setting profile improves interoperability with black. The settings this enables can be found [here](https://github.com/PyCQA/isort/blob/main/isort/profiles.py#L4-L11).

The `float_to_top` setting will move all imports in the module to the top of the file.

# pylint

> Pylint is a Python static code analysis tool which looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions.

Besides checking your code for actual errors that would immediately crash at runtime, I also appreciate some of the more opinionated design lints.

For example, if your class only has two functions, and one of those functions is `__init__`, it probably shouldn't be a class. Or if you have a method that takes in `self` but doesn't use it, it could be a function instead. Other checks include
- Code duplication
- Code complexity
- Docstring formatting

Pylint also provides [optional extensions](https://pylint.pycqa.org/en/v2.14.0-b1/technical_reference/extensions.html) which I try to enable as many as possible. Of note is the docstring extension which checks docstrings match the function signature.

Errors can be disabled per-line by adding `# pylint: disable=no-member,another-one` at the end of a line.

Errors can be disabled per-block by adding `# pylint: disable=no-member` to it’s own line at the beginning and re-enabling at the end with `# pylint: enable=no-member`


# mypy

> Mypy is an optional static type checker for Python. You can add type hints (PEP 484) to your Python programs, and use mypy to type check them statically. Find bugs in your programs without even running them!

Setting the strict flag will set all of mypy’s most strict type-checking options. The list of options can be seen by running `mypy --help | grep -A 8 'Strict mode;'`. These flags include forcing all function signatures to have type hints, among others.

Type errors can be ignored per line by adding `# type: ignore[error-name]` to the end of a line.


# Bandit

https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing

# Automating with invoke + tasks.py

> Invoke is a task execution tool & library, drawing inspiration from various sources to arrive at a powerful & clean feature set.

Most of the Python I write are one-off scripts or small projects and I don't want to copy the same `pyproject.toml` file into each one. Instead I place it in my home directory and pass it in directly as an argument to all the tools. `invoke` is a tool that allows you to define a `tasks.py` file with commands you want to run. Then from any folder I can just run `invoke fmt` or `invoke check` to run my linters. My `tasks.py` file can be found [here](https://github.com/benburk/dotfiles/blob/master/python/tasks.py).