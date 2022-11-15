# Time Calculator

Write a function named add_time that takes in two required parameters (start time and duration time) and one optional parameter (starting day of the week). The function should add the duration time to the start time and return the result.

## Table of contents

-   [Overview](#overview)
    -   [Rules](#rules)
    -   [Testing](#testing)
    -   [Screenshot](#screenshot)
-   [My process](#my-process)
    -   [Built with](#built-with)
    -   [What I learned](#what-i-learned)
-   [Author](#author)

## Overview

### Rules

- If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

- If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

### Testing

The unit tests for this project are in test_module.py. We are running the tests from test_module.py in main.py for your convenience. The tests will run automatically whenever you hit the "run" button. Alternatively you may run the tests by inputting pytest in the console.

### Screenshot

![](/time_calculator.png)

### Executing program

-   Run the main.py script in terminal

```
python main.py
```

## My process

### Built with

-   Python 3.9.12 

### What I learned

Cycle a string using a dictionary.

```python
period_cycle = {'AM': 'PM', 'PM': 'AM'}
period = 'AM'
period = period_cycle[period]
```

## Authors

-   Project assigned by FreeCodeCamp - [FreeCodeCamp](https://www.freecodecamp.org/learn/)
-   Marco Cámez - [Codeline0](https://github.com/Codeline0)