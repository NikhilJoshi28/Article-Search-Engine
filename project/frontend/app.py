from flask import Flask, render_template, request, url_for, redirect, session, app
import sys
sys.path.insert(0,'/home/tex/Documents/IR/Wikipedia-Search-Engine/project/rankretrievalmodel/English/')

from query_processing import query_reduction
sys.path.insert(1,'/home/tex/Documents/IR/Wikipedia-Search-Engine/project/rankretrievalmodel/Arabic/')
from query_processor import loadModel,QueryProcessor

app = Flask(__name__, static_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index/',methods=['GET','POST'])
def ind():
    return render_template("index.html")

@app.route('/search1/',methods=['GET','POST'])
def search1():
    try:
        if request.method == "POST":
            english_query = request.form['query1']
            print(english_query)
            runQuery = query_reduction()
            filter_query = runQuery.reducedQuery_stopwords(english_query)
            print(filter_query)
            stemmed_query = (runQuery.reducedQuery_stemming(filter_query))
            print(stemmed_query)
            #print("asd")
            return render_template("english_search.html")
    except Exception as e:
        print(e)
        return render_template("index.html")

@app.route('/search2/',methods=['GET','POST'])
def search2():
    try:
        if request.method=="POST":
            arabic_query = request.form['query2']
            print(arabic_query)
            processed_corpus_path = '/home/tex/Documents/IR/proc_data'
            inverted_index_path = '/home/tex/Documents/IR/inverted_index'
            model = loadModel(inverted_index_path)
            qp = QueryProcessor(arabic_query, model, processed_corpus_path)
            ans = qp.search()
            print(ans)
            return render_template("arabic_search.html",Doc_Name=ans)
    except Exception as e:
        print(e)
        return render_template("index.html")

@app.route('/Wild_Card/',methods=['GET','POST'])
def WildCard():
    try:
        if request.method=="POST":
            arabic_query = request.form['query1']
            output_list = []
            #print(output_list)
            print(arabic_query)
            return render_template("WCsearchResult.html")
    except Exception as e:
        print(e)
        return render_template("Wild_Card.html")

    return render_template("Wild_Card.html")

@app.route('/WCsearchResult/',methods=['GET','POST'])
def wc():
    return render_template("WCsearchResult.html")

@app.route('/Compare_Article.html/',methods=['GET','POST'])
def CompareArticle():
    return render_template("Compare_Article.html")

if __name__=='__main__':
    app.run(host='0.0.0.0', port=2809, debug=True, threaded=True)