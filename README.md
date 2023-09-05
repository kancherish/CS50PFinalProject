 #### PDF SEACHER
 #### Video Demo:  [video link](https://youtu.be/ueEssV-Dk30?si=xribv6oNNjaeD-yH)

#### Description:
This is pdf searcher which searches your whole device or specific location on your device
    based on your choice

    So, first of all I like to give some info on Why I created this.so I am college going student
    and i got lot of notes as pdf format and whenever i want to read some topic i got always confuse
    on which pdf contain which topics and i have to manually have to go to multiple pdfs to find a
    certain topic which is a boring and time-consuming task for me so i thought why don't create a
    python program to do it and here is it (also as my cs50P final project;)) my pdf searcher

    so lets get to it description of working part of program:

    so our program starts with prompting user with search area i.e scope of searching area of our
    program ,here user have two choices:
>1.root:searches whole device's files and folder

>2.any-file-location:here user can enter his choice location where user wants to search and searches
    all file  from that location

    after asking for search scope the program will give you 3 function option with its
    coresponding keyword and then prompt for keyword and user can enter keyword of own
    choice keyword for their choice coresponding function to run

the three function that will be prompted

>show all files(sh)

>find based on file name(f)

>find based on content in it(fc)

```
    Show all Files:

         As the name suggests this function shows all the pdf file available within
         the search scope of the program given and will be printing "No Files Found"
         if no pdf files are available within the given search scope
         note:giving root will scan the whole device directory

```
```
    Find based on Filenames:

         this function searches the files based on file name and the gives results
         containing similiar the keyword given to it and will be printing "No Files Found"
         if no pdf files having keyword corresponding file name are available within
         the given search scope
         Note: if you wanna find filename "A guide to python" then keyword
         like:"guide","python" will able to find while keyword like:'gd',
         'pyhon' would be failed to do task.

```

```
    Find based on content in it:

      this is the main function of our program and why i created it,So it takes keyword
      and search that keyword in all pdf files available in search scope and shows all file,
      fileLocation and number of time that word had occured in that file(watch video demo for
      a better visual example of it) and print "No Match Found" if no pdf files found contaning
      that keyword in coresponding search scope

```

   Now lets see a brief overview of code structure and designing:

   note:the program structure was being made keepig in mind
   cs50p final project instruction and to run it with pytest
   so would have done many things not that way ,that have been done here

   So lets get to basic structure of this program ,so this program have

   scope function:

         this function is made for deciding scope of search of program would have simply
         made a global keyword with ifelse shorthand but have to respect cs50p guidlines
         and made work it pytest i came up this solution so ther is nothing much about this function

         arguments take:location(string)
         return value:search_scope based on location(string)

   show and find function:

          show and find are very simliar and simple functions so lets get it finsih it real quick
          both the function simultaneously

          >show(search_scope)

          So the show function takes one argument search_scope and then finds all pdfs
          available within the search scope and appends all them to a python list named results and then returns a list
          containg all the location where pdfs are located to main function and then that list is iterated and
          shown to the user

          arguments take:location(string)
          return value:results(list) if 1 or more file found else returns none

          >find(keyword,search_scope)

          the working of find function is very similiar to show function, it also find all available
          pdfs available within the search scope except it takes a additonal argument named keyword
          and then appends only those location which have file coresponding to the given Keyword
          and then do same as show function

          arguments take:location(string),keyword(string)
          return value:results(list) if 1 or more file found else returns none

   Findcontent function:

               >Findcontent(keyword,search_scope)

               this function takes two arguments which are keyword and search_scope
               so what it does it its first creates a empty dictionary named results
               then it calls the show function and the search_scope taken as argument
               has been given as argument to show function and stores the result to the
               a list named locations and and if no pdf files are available then an empty
               dictionary is returned

               else if show doesnt return a empty list then list will be stored in a variable
               named locations and then iteration will start on that locations as:

               >for location in locations:

               and then on each location we will reading all pdf files available through pypdf
               libary module named pdfreader and create a pdfreader object in try except block
               as if pdf is empty it could raise error the structure is as:

               >try:
               >    pdfreader=pd.PdfReader(location)
               >except:
               >    continue

               if error is raised then whole iteration is skipped and will go to next iteration

               then after through pdfreader object we would page reader function and iterate over
               it to find the keyword given by the user and then if keyword is matched it added to
               the result dictionary and if the file already exist then the value is updated i.e word
               ocurence is incremented and after loop is completed the dictionary is returned

               ok here some of may argue that instead of creating a result type dictionary I should
               have created my own class named result with attributes filename,location,word_ocurrence
               but throught dont know why but program was getting more slower So I decided to choose
               dictionary
            arguments take:keyword(string),location(string)
           return value:results(Dictionary)



Main Function:


               so this is the main function where all other function are called and its starts
               with asking user with search_scope given value to scope function and creating
               search_scope which will be given to further to all functions in program then
               a through tabulate libary a function a predefined python list of actions is presented
               to the user and user is prompted with choice of which function is they wanna use and
               then the choice string is matched with match case  and corresponding function is runed
               and prints invalid choice if invalid keyword is chosen

               if valid function is chosen by user that function will run with search_scope and keyword will be prompted
               on find and findcontent function and then return results will be iterated and printed or no found related
               will be printed if functions returns none


P.S.-This was my life's first programming project and i know i would have made a lot of unintenional noobie mistakes so
some review and criticism is much appreciated.

Thanks for Reading!

