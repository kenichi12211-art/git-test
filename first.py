
from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/",methods =["GET","POST"])
def word():
    word1="明日は上原うどんに行きます"
    word2="かけうどんを食べます"
    word3="天ぷらも一つ食べます"
    if request.method== "POST":
        word1=request.form.get("word1")
        word2=request.form.get("word2")
        word3=request.form.get("word3")
    return render_template("index3.html",word1=word1,word2=word2,word3=word3)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)
