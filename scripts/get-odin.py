from sys import argv
from requests import get
from os import path, makedirs, listdir
from zipfile import ZipFile
from re import compile
from shutil import move, rmtree

FOLDER = ".cache/" # folder containing temporarily downloaded files.
FOLDER_THEMES_WORDPRESS_ODIN = "../wp-content/themes/odin/" # path to Odio themes folder from WordPress container.
NAME_FILE = "odin.zip" # name of the downloaded file .zip of the official website
URL_ODIN_FRAMEWORK = "https://api.github.com/repos/wpbrasil/odin/zipball/" # URL of the official website framework.

def __download_odin__(url):
  """
    Download the Odin Framework zip file and add it to the .cache/ folder.

    Parameters
    ----------
    url : string
      File URL to download.

    Returns
    -------
    bool
      Return True if you have successfully downloaded False and otherwise.
  """
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
      print("error download odin, verify url or version")


  return completed_download

def __extract_odin__(file):
  """
    Extracting zip file in .cache/ folder.

    Parameters
    ----------
    file : string
      Path of the file to be extracted.

    Returns
    -------
    bool
      Return True if you have successfully extracted False and otherwise.
  """
  completed_extract = False
  print("extract odin framework, file: {}".format(file))
  
  try:
    archive = ZipFile(file, "r")
    archive.extractall(FOLDER)
    archive.close()
    completed_extract = True
  except:
    print("error extract odin, verify download successful")

  return completed_extract

def __move_odin__(folder):
  """
    Move cache folder to the Odin themes folder of the wordpress container (wp-cotent/themes/odin/).

    Parameters
    ----------
    folder : string
      Path to container folder Odin themes.

    Returns
    -------
    bool
      Return True if you have successfully moved False and otherwise.
  """
  completed_move = False
  print("move folder odin for folder wordpress themes")

  regex_folder_odin = compile("wpbrasil-odin-*")
  folder_odin = filter(regex_folder_odin.match, listdir(folder))
  if(len(folder_odin) > 0):
    folder_odin = folder_odin[0]
    try:
      move(folder + folder_odin, FOLDER_THEMES_WORDPRESS_ODIN)
      completed_move = True
    except:
      print("error move odin, verify extract successful")
  
  return completed_move

def __get_odin__(version):
  """
    Capture the Odin of the official website and move to the wordpress container themes folder (wp-content/themes/odin/).

    Parameters
    ----------
    version : string
      Odin's version.

    Returns
    -------
    bool
      Return True if you have successfully get False and otherwise.
  """
  completed_get = False
  url = URL_ODIN_FRAMEWORK + version
  print("get odin framework")

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

def __remove_cache__(folder):
  """
    Remove folder used for caching.

    Parameters
    ----------
    folder : string
      Folder path to delete.
    Returns
    -------
    bool
      Return True if you have successfully removed False and otherwise.
  """
  completed_remove_cache = False
  print("remove cache folder")

  try:
    rmtree(folder)
    completed_remove_cache = True
  except:
    print("error remove cache folder, verify PATH folder cache")

  return completed_remove_cache

def __main__():
  version = ""
  if(len(argv) > 1):
    version = argv[1]
  if(__get_odin__(version)):
    print("get odin done!")
    if(__remove_cache__(FOLDER)):
      print("cache remove done!")
    else:
      print("error remove cache!")    
  else:
    print("error get odin!")

__main__()