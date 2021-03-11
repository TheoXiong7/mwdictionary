# About

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dbd964c0d12e442cbe461aa11d915e92)](https://app.codacy.com/gh/TheoXiong7/mwdictionary?utm_source=github.com&utm_medium=referral&utm_content=TheoXiong7/mwdictionary&utm_campaign=Badge_Grade_Settings)

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
