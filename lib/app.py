import csv

surveryFileName = raw_input("Enter survery file name here: ")
resultFileName = raw_input("Enter results file name here: ")

#change according to the path that its placed at the time of running the code
path = "/Users/anitanaseri/desktop/CLI_application_code_challenge/example-data/"

#reading the survey file and stroing it in dictionary
with open(path + surveryFileName + ".csv", 'rb') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    surveyDict = {name: [] for name in csv_reader.fieldnames}
    line_count = 0
    for row in csv_reader:
        for name in csv_reader.fieldnames:
            surveyDict[name].append(row[name])
        line_count +=1


# reading the results file
with open(path + resultFileName + ".csv", 'rb') as csvfile:
    resultTitles = ["email", "employee_id", "submitted_at",
    "answers", "ratingquestion"]
    csv_reader = csv.reader(csvfile, delimiter=',')
    resultsDict = {name: [] for name in resultTitles}

    # store the number of questions that are rating questions
    for i in range(line_count):
        if (surveyDict["type"][i] == "ratingquestion"):
                resultsDict["ratingquestion"].append(i)
        else:
            continue

    # adding nested list with a list for each question to store its Answers
    # like if its 4 questions it'll be [[],[],[],[]]
    list = []
    for i in range(len(resultsDict["ratingquestion"])):
        list.append([])
    resultsDict["answers"] = list

    for row in csv_reader:
        for name in resultTitles:
            #if the sumitted time is empty skipped that person
            if (row[2] == ""):
                continue;
            else:
                if (name == "email"):
                    resultsDict[name].append(row[0])
                elif (name == "employee_id"):
                    resultsDict[name].append(row[1])
                elif (name == "submitted_at"):
                    resultsDict[name].append(row[2])
                elif (name == "answers"):
                    for j in range(len(resultsDict["ratingquestion"])):
                        # plus 3 beacuse answers start at index 3
                        #if the answer was empty skip it
                        if (row[j+3] == ""):
                            continue;
                        else:
                            resultsDict[name][j].append(row[j+3])

#number of participants
print "Number of people participating is",
print len(resultsDict["submitted_at"])

if len(resultsDict["submitted_at"]) !=0:
    for k in range(len(resultsDict["answers"])):
        sum = 0
        for i in resultsDict["answers"][k]:
            sum += int(i)
        print "The average for the question number",
        print k+1,
        print "rating question is",
        print float(sum)/len(resultsDict["answers"][k])
else :
    print "didnt find any submitted answers"
