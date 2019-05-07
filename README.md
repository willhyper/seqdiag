# seqdiag
sequence diagram of REST request
![alt text](https://github.com/willhyper/seqdiag/blob/master/screenshot.png)


## setup
```python
pipenv install
```

## launch server
use one process to launch server
```python
python -m seqdiag
```

## client sends request
use another process to send requests as clients
```python
python test_post.py
```

## result
browse to http://localhost:8000/
