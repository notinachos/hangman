# hangman
A hangman clone, written in Python3 for the terminal.

## Usage
Run hangman.py from a terminal using Python3:
```bash
python3 ./hangman.py
```
## Adding Words
Words have been encoded in ROT13 to avoid giving away the answers. 
Python has a built-in ROT13 translator. Here is how to use it:
```python
import codecs
new_word = input('type a word: ')
print('Your ROT13 encoded word is: ' + codecs.encode(new_word, 'rot_13'))
```

