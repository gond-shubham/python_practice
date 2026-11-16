# Python Regular Expressions

This folder contains Python practice programs focused on Regular Expressions (RegEx) using Python's built-in `re` module.

The purpose is to understand how to create search patterns, match text, extract information, validate strings and perform text manipulation.

## Topics Covered

### 1. Basic Pattern Matching
- Understanding regular expressions
- Using the `re` module
- `re.search()`
- `re.match()`
- `re.fullmatch()`
- Understanding match objects
- Accessing matched content using `group()`

### 2. Character Classes
- Custom character classes using `[ ]`
- Digit matching using `[0-9]`
- Predefined character classes:
  - `\d` and `\D`
  - `\w` and `\W`
  - `\s` and `\S`
- Matching specific characters and character combinations

### 3. Quantifiers
- Exact matching using `{n}`
- Range matching using `{n,m}`
- One or more occurrences using `+`
- Zero or more occurrences using `*`
- Optional occurrences using `?`
- Understanding greedy matching

### 4. Anchors
- Start of string using `^`
- End of string using `$`
- Matching patterns at specific positions
- Using anchors for exact string validation

### 5. Groups
- Capturing groups using `( )`
- Named capturing groups using `(?P<name>...)`
- Accessing groups using `group()` and `groups()`
- Retrieving named groups using `groupdict()`
- Non-capturing groups using `(?:...)`

### 6. Lookaheads
- Positive lookahead `(?=...)`
