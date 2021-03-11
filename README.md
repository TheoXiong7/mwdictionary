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
```python
output > a group of animals (such as birds or sheep) assembled or herded together
```
