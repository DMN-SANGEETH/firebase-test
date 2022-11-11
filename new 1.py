import pyrebase

config = {
  "apiKey": "AIzaSyB527hyMfhmS-ZuZAC4s7_rnzz4OjQJbIc",
  "authDomain": "dnnstore-2dfff.firebaseapp.com",
  "databaseURL": "https://dnnstore-2dfff.firebaseio.com",
  "storageBucket": "dnnstore-2dfff.appspot.com"
}

firebase = pyrebase.initialize_app(config)