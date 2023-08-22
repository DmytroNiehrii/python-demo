import webbrowser

def validator(func):
  def wrapper(url):
    print("Decorator before")
    func(url)
    print("Decorator after")
  return wrapper

@validator
def open_url(url):
  webbrowser.open(url)

open_url('https://itproger.com')