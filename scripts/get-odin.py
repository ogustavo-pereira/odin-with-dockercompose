from sys import argv
from requests import get
from os import path, makedirs, listdir
from zipfile import ZipFile
from re import compile
from shutil import move

FOLDER = ".cache/"
FOLDER_THEMES_WORDPRESS_ODIN = "../wp-content/themes/odin/"
NAME_FILE = "odin.zip"

def __download_odin__(url):
  completed_download = False
  if(url):
    print("download odin framework, url: {}".format(url))
    response = get(url)

    if(not path.exists(FOLDER)):
      makedirs(FOLDER)
    
    try:
      with open(FOLDER + NAME_FILE, "wb") as code:
        code.write(response.content)

      completed_download = True
    except:
      completed_download = False


  return completed_download

def __extract_odin__(file):
  completed_extract = False
  print("extract odin framework, file: {}".format(file))
  
  try:
    archive = ZipFile(file, "r")
    archive.extractall(FOLDER)
    archive.close()
    completed_extract = True
  except:
    completed_extract = False

  return completed_extract

def __move_odin__(folder):
  completed_move = False

  regex_folder_odin = compile("wpbrasil-odin-*")
  folder_odin = filter(regex_folder_odin.match, listdir(folder))
  if(len(folder_odin) > 0):
    folder_odin = folder_odin[0]
    try:
      move(folder + folder_odin, FOLDER_THEMES_WORDPRESS_ODIN)
      completed_move = True
    except:
      completed_move = False
  
  return completed_move

def __get_odin__(version):
  completed_get = False
  url = "https://api.github.com/repos/wpbrasil/odin/zipball/" + version
  if(__download_odin__(url)):
    print("download done!")
    if(__extract_odin__(FOLDER + NAME_FILE)):
      print("extract done!")
      if(__move_odin__(FOLDER)):
        print("move folder done!")
        completed_get = True
      else:
        print("move folder fail!")
    else:
      print("extract fail!")
  else:
    print("download fail!")
  return completed_get

def __main__():
  version = ""
  if(len(argv) > 1):
    version = argv[1]
  if(__get_odin__(version)):
    print("get odin done!")
  else:
    print("error get odin!")

__main__()