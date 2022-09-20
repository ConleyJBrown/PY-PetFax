from petfax import create_app
app = create_app()

# index route
@app.route('/')
def index(): 
    return 'Hello, this is PetFax!'



