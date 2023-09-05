from tabulate import tabulate
import pypdf as pd
import os



def main():
    search_scope=scope(input("enter search area(root/<your_location>): "))
    actions=[["sh","show all pdf files available on device"],
             ["f","Finds the pdf files on filename"],
             ["fc","Find The pdf files on content"]]

    print(tabulate(actions, headers=["Key","Description"],tablefmt="double_grid"))

    user_choice=input("Your Choice: ").lower()

    match user_choice:
        case "sh":
            if locations:=show(search_scope):
                for location in locations:
                    print(location)
            else:
                print("No pdf files available")
        case "f":
            if locations:=find(input("enter filename: "),search_scope):
                for location in locations:
                    print(location)
            else:
                print("No Files Found")

        case "fc":
             if results:=Findcontent(input("enter text you wanna find: "),search_scope):
                for i,result in enumerate(results):
                    print(f"{i+1}.\nFilename:{result.split('/')[-1]}\nLocation: {result}\nWord Occured: {results[result]}\n")
             else:
                 print("No Match Found")
        case _:
            print("Invalid Choice")


def scope(scope):
    return "/" if scope=="root" else scope


def show(search_scope):
    result=[]
    for root, _, files in os.walk(search_scope):
      for file in files:
        if ".pdf" in file:
            result.append(os.path.join(root, file))
    return result

def find(name,search_scope):
     result=[]
     for root, _, files in os.walk(search_scope):
        for file in files:
            if f"{name.lstrip('.pdf')}" in file and file.endswith(".pdf"):
                result.append(os.path.join(root, file))
     return result

def Findcontent(keyword,search_scope):
    results={}
    if locations:=show(search_scope):
        for location in locations:
            try:
                pdfreader=pd.PdfReader(location)
            except:
                continue
            for page in pdfreader.pages:
                contents=page.extract_text().split("\n")
                for text in contents:
                    if keyword in text:
                        if location in results:
                            results.update({location:results[location]+1})
                        else:
                            results.update({location:1})
    return results




if __name__=="__main__":
    main()