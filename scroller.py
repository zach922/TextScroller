import pyrebase

config = {
	"apiKey" : "JMAydJGGOw3t46ePB4Olipr3FYAKfEMgvgUuDn7M" ,
	"authDomain" : "text-scroller-ccc3c.firebaseapp.com",
	"databaseURL" : "https://text-scroller-ccc3c-default-rtdb.firebaseio.com",
	"storageBucket" : "text-scroller-ccc3c.appspot.com"
}

db = pyrebase.initialize_app(config)
