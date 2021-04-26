# Lecture Learning Objectives

## Lecture 1: Python Basics

- Create, describe and differentiate standard Python datatypes such as `int`, `float`, `string`, `list`, `dict`, `tuple`, etc.
- Perform arithmetic operations like `+`, `-`, `*`, `**` on numeric values.
- Perform basic string operations like `.lower()`, `.split()` to manipulate strings.
- Compute boolean values using comparison operators operations (`==`, `!=`, `>`, etc.) and boolean operators (`and`, `or`, `not`).
- Assign, index, slice and subset values to and from tuples, lists, strings and dictionaries.
- Write a conditional statement with `if`, `elif` and `else`.
- Identify code blocks by levels of indentation.
- Explain the difference between mutable objects like a `list` and immutable objects like a `tuple`.

## Lecture 2: Loops & Functions

- Write `for` and `while` loops in Python
- Identify iterable datatypes which can be used in `for` loops.
- Create a `list`, `dictionary`, or `set` using comprehension.
- Write a `try`/`except` statement.
- Define a function and an anonymous function in Python.
- Describe the difference between positional and keyword arguments.
- Describe the difference between local and global variables.
- Apply the `DRY principle` to write modular code.
- Assess whether a function has side effects.
- Write a docstring for a function that describes parameters, return values, behaviour and usage.

## Lecture 3: Unit Tests & Classes

- Formulate a test case to prove a function design specification.
- Use an `assert` statement to validate a test case.
- Debug Python code with the `pdb` module, or by using `%debug` in a Jupyter code cell.
- Describe the difference between a `class` and a `function` in Python.
- Be able to create a `class`.
- Differentiate between `instance attributes` and `class attributes`.
- Differentiate between `methods`, `class methods` and `static methods`.
- Understand and implement `subclassing`/`inheritance` with Python classes.

## Lecture 4: Style Guides, Scripts & Imports

- Describe why code style is important.
- Differentiate between the role of a linter like `flake8` and an autoformatter like `black`.
- Implement linting and formatting from the command line or within Jupyter or another IDE.
- Write a Python module (`.py` file) in VSCode or other IDE of your choice.
- Import installed or custom packages using the `import` syntax.
- Explain the notion of a reference in Python.
- Explain the notion of scoping in Python.
- Anticipate whether changing one variable will change another in Python.
- Anticipate whether a function changes the caller's version of an argument variable in Python.
- Select the appropriate choice between `==` and `is` in Python.

## Lecture 5: Introduction to NumPy

- Use NumPy to create arrays with built-in functions inlcuding `np.array()`, `np.arange()`, `np.linspace()` and `np.full()`, `np.zeros()`, `np.ones()`.
- Be able to access values from a NumPy array by numeric indexing and slicing and boolean indexing.
- Perform mathematical operations on and with arrays.
- Explain what broadcasting is and how to use it.
- Reshape arrays by adding/removing/reshaping axes with `.reshape()`, `np.newaxis()`, `.ravel()`, `.flatten()`.
- Understand how to use built-in NumPy functions like `np.sum()`, `np.mean()`, `np.log()` as stand alone functions or as methods of numpy arrays (when available).

## Lecture 6: Introduction to Pandas

- Create Pandas series with `pd.Series()` and Pandas dataframe with `pd.DataFrame()`.
- Be able to access values from a Series/DataFrame by indexing, slicing and boolean indexing using notation such as `df[]`, `df.loc[]`, `df.iloc[]`, `df.query[]`.
- Perform basic arithmetic operations between two series and anticipate the result.
- Describe how Pandas assigns dtypes to Series and what the `object` dtype is.
- Read a standard .csv file from a local path or url using Pandas `pd.read_csv()`.
- Apply basic operations to a dataframe like `.min()`, `.mean()`, `.sort_values()`, etc.
- Explain the relationship and differences between `np.ndarray`, `pd.Series` and `pd.DataFrame` objects in Python.

## Lecture 7: Basic Data Wrangling with Pandas

- Inspect a dataframe with `df.head()`, `df.tail()`, `df.info()`, `df.describe()`.
- Obtain dataframe summaries with `df.info()` and `df.describe()`.
- Manipulate how a dataframe displays in Jupyter by modifying Pandas configuration options such as `pd.set_option("display.max_rows", n)`.
- Rename columns of a dataframe using the `df.rename()` function or by accessing the `df.columns` attribute.
- Modify the index name and index values of a dataframe using `.set_index()`, `.reset_index()` , `df.index.name`, `.index`.
- Use `df.melt()` and `df.pivot()` to reshape dataframes, specifically to make tidy dataframes.
- Combine dataframes using `df.merge()` and `pd.concat()` and know when to use these different methods.
- Apply functions to a dataframe `df.apply()` and `df.applymap()`
- Perform grouping and aggregating operations using `df.groupby()` and `df.agg()`.
- Perform aggregating methods on grouped or ungrouped objects such as finding the minimum, maximum and sum of values in a dataframe using `df.agg()`.
- Remove or fill missing values in a dataframe with `df.dropna()` and `df.fillna()`.
- Understand what the `SettingWithCopyWarning` means in Pandas.

## Lecture 8: Advanced Data Wrangling with Pandas

- Manipulate strings in Pandas by accessing methods from the `Series.str` attribute.
- Understand how to use regular expressions in Pandas for wrangling strings.
- Differentiate between datetime object in Pandas such as `Timestamp`, `Timedelta`, `Period`, `DateOffset`.
- Create these datetime objects with functions like `pd.Timestamp()`, `pd.Period()`, `pd.date_range()`, `pd.period_range()`.
- Index a datetime index with partial string indexing.
- Perform basic datetime operations like splitting a datetime into constituent parts (e.g., `year`, `weekday`, `second`, etc), apply offsets, change timezones, and resample with `.resample()`.
- Make basic plots in Pandas by accessing the `.plot` attribute or importing functions from `pandas.plotting`.
