# web-scrapping
start to learn web scrapping
## Modules:
### webbrowser
  ```sh
  >>> import webbrowser
  >>> webbrowser.open('https://inventwithpython.com/')
  ```
  
### requests
  *requests.get()
  ```sh
  >>> import requests
  >>> res = requests.get(' ')
  >>> res.status_code == requests.codes.ok
  >>> print(res.text)
  >>> print(r.json())
  ```
  *checking for errors
  ```sh
  try:
    res.raise_for_status() 
  except Exception as exc:
    print('There was a problem: %s' % (exc))
  ```
  *save files
 ```sh
  >>> import requests
  >>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt') 
  >>> res.raise_for_status()
  >>> playFile = open('RomeoAndJuliet.txt', 'wb')
  >>> for chunk in res.iter_content(100000):
          playFile.write(chunk)
  100000
  78981
  >>> playFile.close()
  ```
  
 ### bs4 parcing html
