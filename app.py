from flask import Flask,render_template,request,send_file
import os
app = Flask(__name__)




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generate" , methods=["POST"])
def generate():

    f = os.listdir("static")

    for file in f:
        filepath = os.path.join("static", file)
        if os.path.isfile(filepath):
            os.unlink(filepath)
            print("file deleted Succesfully")
    l = []
    if request.method == "POST":
        count = 0
        
        
        b = {}
        a = request.form.to_dict()
        print(a)
        files = request.files
        for file in files:
            # Save the file here
            if(file == "background"):
                b["bg"] = request.files[file].filename
                temp = request.files[file]
                temp.save("static/"+temp.filename)
            else:
                temp = request.files[file]
                temp.save("static/"+temp.filename)
            l.append(temp.filename)
        
        
        
        

        html = open("static/index.html","w")
        html.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<meta http-equiv='X-UA-Compatible' content='IE=edge'>\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n<title>Website (U)</title>\n<link rel='icon' type='image/x-icon' href='Images/logo.png'>\n</head>\n<body>\n")
        html.write("<style>\n*{color:"+a['font-color']+";font-family:"+a["font-family"]+";text-align:center;}\nimg{border-radius:10px;height:250px;width:250px;}</style>")
        if(a["background-select"] == "color"):
            background_color = a["background"]
            html.write("<style>\nbody{background-color:"+background_color+";}</style>")
        else:    
            html.write("<style>\nbody{background:url("+b['bg']+");\nbackground-size: cover;\nbackground-repeat: no-repeat;\n}</style>")
        html.close()

        html = open("static/index.html","a+")



        for i in a.keys():
            if(a[i] == "h1"):
                print(f"<h1>{a[f'{i}-input-text']}</h1>")
                html.write(f"\n<h1>{a[f'{i}-input-text']}</h1>")
            elif(a[i] == "para"):
                print(f"\n<p>{a[f'{i}-input-text']}</p>")
                html.write(f"<p>{a[f'{i}-input-text']}</p>")
            elif(a[i] == "h3"):
                print(f"\n<h3>{a[f'{i}-input-text']}</h3>")
                html.write(f"<h3>{a[f'{i}-input-text']}</h3>")
            elif(a[i] == "button"):
                print(f"\n<a href={a[f'{i}-input-text'].split(',')[0]}>{a[f'{i}-input-text'].split(',')[1]}</a>")
                html.write(f"\n<a href={a[f'{i}-input-text'].split(',')[0]}>{a[f'{i}-input-text'].split(',')[1]}</a>")
            elif(a[i] == "image"):
                # if(l[count] != b['bg']):
                if(a["background-select"] == "color"):
                    print(f"<img src='static/{l[count]}' >")
                    html.write(f"\n<img src='{l[count]}' height='100px' width='100px' >")
                else:
                    if(l[count] != b['bg']):
                        print(f"<img src='static/{l[count]}' >")
                        html.write(f"\n<img src='{l[count]}' height='100px' width='100px' >")
                count +=1
            elif(a[i] == "input"):
                name = str(i)+"-input-text"
                html.write(f'\n<input type="{a[name]}" name="input" id="in" placeholder="Enter" style="padding:15px;">')


            
        html.write("</body>\n</html>")
        html.close()



        print(l)
        return render_template("result.html")
    else:
        return "Error"
@app.route("/download")
def download():
    path = r"static\index.html"
    return send_file(path,as_attachment=True)

@app.route("/index")
def index():
    return render_template("static/index.html")


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')




"""

    open Sans : <style>
                @import url('https://fonts.googleapis.com/css2?family=Open+Sans&family=Poppins:wght@300&display=swap');
                </style>

    
    Yaseabu  : <style>
                @import url('https://fonts.googleapis.com/css2?family=Open+Sans&family=Poppins:wght@300&family=Ysabeau:wght@300&display=swap');
                </style>

    Satisfy   :   <style>
                @import url('https://fonts.googleapis.com/css2?family=Open+Sans&family=Poppins:wght@300&family=Satisfy&family=Ysabeau:wght@300&display=swap');
                </style>



    


"""
