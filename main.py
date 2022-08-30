from what_todo import application

app = application.create()

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)
