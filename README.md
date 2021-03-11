[![Codacy Badge](https://app.codacy.com/project/badge/Grade/701232abf9014344a2c0fa4c235e0a9a)](https://www.codacy.com/gh/TheoXiong7/mwdictionary/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=TheoXiong7/mwdictionary&amp;utm_campaign=Badge_Grade)
# About
I made this Merriam-Webster dictionary api wrapper for python. 
Go to https://dictionaryapi.com/ to retrieve a free api key.

## Usage
```python
import mwdictionary as mw
definition = mw.define('flock', 'yourkeyhere')
```
## Data Structure
```python
{
'word': 'flock', 
'definition': 'a group of animals (such as birds or sheep) assembled or herded together',
'type': 'noun',
'offensive': 'False'
}
```

## Example
```python
import mwdictionary as mw
definition = mw.define('flock', 'yourkeyhere')
print(definition['definition'])
```
```
output > a group of animals (such as birds or sheep) assembled or herded together
```
