# Automated Scripts :rocket:
You can use a ready script :fire: written in `Python` to download any version of **Odin Framework** using the commands: 
```shell
$ cd scripts/
$ python get-odin.py # capture the latest version
```

Or if you want to capture an old version: 
```shell
$ cd scripts/
$ python get-odin.py 1.0.0 # example capture for version 1.0.0 
```
## Dependencies
* [Python 3](https://www.python.org/download/releases/3.0/)
* [requests](http://docs.python-requests.org/en/master/)
* [zipfile](https://docs.python.org/3/library/zipfile.html)
* [shutil](https://docs.python.org/3/library/shutil.html)

## More informations
You can get as many versions of the **Odin Framework** as you want :heavy_check_mark: \
Only equal versions are not accepted :heavy_multiplication_x:

After running the script... :running: \
To check if everything went well, just open the folder `wp-contents/themes/odin/` and check if the version was added to the folder successfully, then just activate the theme with the added version :ballot_box_with_check:
