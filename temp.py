def analyse(query):
    print(f"Analyzing ---> {query}")
    """
    Analyses the type of command provided. Categorizes it to its type.
    """
    pass
    # if (query == "exit"):
    #     features.exit_assist()

    # if ("search" in query):
    #     try:
    #         patt = re.compile(r"search ")
    #         matches = patt.finditer(query)

    #         temp_1 = None
    #         temp_2 = None

    #         for match in matches:
    #             temp_1 = match.span()

    #             pat = re.compile(r" ")
    #             matche = pat.finditer(query)

    #             count = 0
    #             for matc in matche:
    #                 if count == 3:
    #                     break
    #                 temp_2 = matc.span()
    #                 count += 1

    #         engine = query[temp_1[1]: temp_2[1]].replace("on ", "").replace("for ", "").strip()

    #         patt = re.compile(engine)
    #         matches = patt.finditer(query)
    #         temp_3 = None

    #         for match in matches:
    #             temp_3 = match.span()
    #         query = query[temp_3[1]::].strip().split(" ", 1)[1]
    #         if query.split(" ", 1)[1::] == "for " or query.split(" ", 1)[1::] == "at ":
    #             print("Ok")


    #         request = requests.get("http://" + engine + ".com")
    #         if request.status_code == 200:
    #             features.open_webpage(f"https://{engine}.com/?#q={query}")
    #         else:
    #             speak("The engine you are trying to search on doesn't exists.")

    #     except Exception as e:
    #         print(e)

    # elif ("open" in query):
    #     if (".com" or ".org" or ".net" or ".edu" or ".int" or ".gov" or ".mil" or ".arpa") in query:
    #         speak("Open Webpage!")
    #         query = query.split()
    #         for i in query:
    #             if (".com" or ".org" or ".net" or ".edu" or ".int" or ".gov" or ".mil" or ".arpa") in i:
    #                 query = i
    #                 break

    #         features.open_webpage(query)

    #     elif ("youtube" or "google" or "bing" or "google cloud" or "google developers" or "daily motion" in query.lower()):
    #         query = query.replace("open ", "").replace("hey ", "").replace("jarvis ", "")
    #         web_list = {"youtube": "https://youtube.com", "google": "https://google.com"}

    #         try:
    #             features.open_webpage(web_list[query])
    #         except:
    #             try:
    #                 pass
    #                 raise ValueError
    #             except:
    #                 try:
    #                     request = requests.get("http://" + query + ".com")
    #                     if request.status_code != 200:
    #                         features.open_webpage("https://google.com/?#q=" + query)
    #                         print("google http")
    #                     else:
    #                         features.open_webpage("http://" + query)
    #                 except Exception as e:
    #                     features.open_webpage("https://google.com/?#q=" + query)

    # elif ("wikipedia" in query or "about" in query):
    #     query = query.lower().split()

    #     garbage = ("search", "what", "para", "paragraph", "about", "wikipedia")
    #     for i in range(len(query)):
    #         try:
    #             query = query.remove(garbage[i])
    #         except Exception as e:
    #             pass

    #     query = query[0]

    #     try:
    #         features.search_wiki(query)
    #     except Exception as e:
    #         print(e)
    #         features.open_webpage(f"https://google.com/?#q={query}")

    # elif ("play" in query):
    #     baseDir = r"D:\Images"
    #     print(baseDir)
    #     if True:
    #         features.play_music(baseDir)
    #     elif True:
    #         features.play_video(baseDir)
    

    # elif ("exit" in query):  # To be written as the last condition
    #     features.exit_assist()
