# FTP download script

Download an FTP tree to a local directory

## Usage
```python
python3 download_ftp_tree ftp.something.com /some/directory ../data
```
The code above will look for a directory called `/some/directory/` on the ftp
host `ftp.something.com`, and then duplicate the directory and its entire contents into the sister directory `../data`.

Additional options are available for authentication and more. See help:
```python3 download_ftp_tree -h```

## Dependencies
Requires Python 3. 

## Issues
Should be modified to write to `../data` by default.
