#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import sys
import numpy as np
from sklearn.naive_bayes import GaussianNB


# test fucking github

enron_data = {}

def main(argv=None):
    # print(argv)
    global enron_data
    enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
    print(enron_data)
    #
    # exercise_poi()


    exercise_all_persons()
    exercise_persons_stats(['PRENTICE JAMES', 'COLWELL WESLEY', 'SKILLING JEFFREY K'])
    exercise_persons_compare(['SKILLING JEFFREY K', 'LAY KENNETH L', 'FASTOW ANDREW S'])

    bayes_test()


def bayes_test():
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    Y = np.array([1, 1, 1, 2, 2, 2])
    clf = GaussianNB()
    clf.fit(X, Y)
    print(clf.predict([[-0.8, -1]]))
    clf_pf = GaussianNB()
    clf_pf.partial_fit(X, Y, np.unique(Y))
    print(clf_pf.predict([[-0.8, -1]]))


def exercise_all_persons():
    persons_with_salary = 0
    persons_with_email = 0
    persons_without_payments = 0
    pois_without_payments = 0
    pois = 0
    for p in enron_data:
        if ('salary' in enron_data[p].keys()) and (enron_data[p]['salary'] != 'NaN'):
            persons_with_salary += 1

        if ('email_address' in enron_data[p].keys()) and (enron_data[p]['email_address'] != 'NaN'):
            persons_with_email += 1

        poi = False
        if ('poi' in enron_data[p].keys()) and (enron_data[p]['poi'] == True):
            pois += 1
            poi = True

        if ('total_payments' not in enron_data[p].keys()) or (enron_data[p]['total_payments'] == 'NaN'):
            persons_without_payments += 1
            if poi:
                pois_without_payments += 1

    print("Features for Persons: " + str(len(enron_data['METTS MARK'].keys())))
    print("Persons: " + str(len(enron_data.keys())))
    print("Persons without payments: " + str(persons_without_payments))

    print("POIs at Data: " + str(pois))
    print("POIs at List: " + str(len(poi_names())))
    print("POIs without payments: " + str(pois_without_payments))

    print("Persons with Salary available: " + str(persons_with_salary))
    print("Persons with E-mail available: " + str(persons_with_email))
    print("Persons without payments: " + str(persons_without_payments))
    print("Persons % without payments: " + str(float(persons_without_payments)/len(enron_data.keys())))

    print("POIs without payments: " + str(pois_without_payments))
    print("POIs % without payments: " + str(float(pois_without_payments)/pois))

    print("Persons +10: " + str(len(enron_data.keys())+10))
    print("Persons +10 without payments: " + str(persons_without_payments+10))

    print("POIs +10: " + str(pois + 10))
    print("POIs +10 without payments: " + str(pois_without_payments + 10))



def exercise_persons_compare(person_names_=[]):
    top_payments = ["Someone",0]
    for p in person_names_:
        print(enron_data[p]['total_payments'])
        if enron_data[p]['total_payments'] > top_payments[1]:
            top_payments = [p, enron_data[p]['total_payments']]

    print("Person who got more payments: " + str(top_payments[0]) + " received " + str(top_payments[1]))


def exercise_persons_stats(person_name_=[]):
    for p in person_name_:
        print("Total stock belonging to " + p + ": " + str(enron_data[p]['total_stock_value']))
        print(" Messages from " + p + " to POIs: " + str(enron_data[p]['from_this_person_to_poi']))
        print("Exercised stock belonging to " + p + ": " + str(enron_data[p]['exercised_stock_options']))


def exercise_poi():
    poi_from_pickle = 0
    names_from_pickle = []

    for k, v in enron_data.iteritems():
        names_from_pickle.append(' '.join(k.split(" ")[0:2]))
        if v["poi"] == 1:
            poi_from_pickle += 1

    print("Amount of POI:" + str(poi_from_pickle))

    names_from_list = poi_names()

    print("Amount of POI from List:" + str(len(names_from_list)))


def poi_names():
    names_file = open('../final_project/poi_names.txt', 'r')
    names = []
    poi = 0
    for row in names_file:
        if row[0] == "(":
            names.append(row.split(")")[1].strip().replace(",", "").upper())
            poi += 1 if row[1] == "y" else 0

    return names


def poi_emails():
    email_list = ["kenneth_lay@enron.net",
                  "kenneth_lay@enron.com",
                  "klay.enron@enron.com",
                  "kenneth.lay@enron.com",
                  "klay@enron.com",
                  "layk@enron.com",
                  "chairman.ken@enron.com",
                  "jeffreyskilling@yahoo.com",
                  "jeff_skilling@enron.com",
                  "jskilling@enron.com",
                  "effrey.skilling@enron.com",
                  "skilling@enron.com",
                  "jeffrey.k.skilling@enron.com",
                  "jeff.skilling@enron.com",
                  "kevin_a_howard.enronxgate.enron@enron.net",
                  "kevin.howard@enron.com",
                  "kevin.howard@enron.net",
                  "kevin.howard@gcm.com",
                  "michael.krautz@enron.com"
                  "scott.yeager@enron.com",
                  "syeager@fyi-net.com",
                  "scott_yeager@enron.net",
                  "syeager@flash.net",
                  "joe'.'hirko@enron.com",
                  "joe.hirko@enron.com",
                  "rex.shelby@enron.com",
                  "rex.shelby@enron.nt",
                  "rex_shelby@enron.net",
                  "jbrown@enron.com",
                  "james.brown@enron.com",
                  "rick.causey@enron.com",
                  "richard.causey@enron.com",
                  "rcausey@enron.com",
                  "calger@enron.com",
                  "chris.calger@enron.com",
                  "christopher.calger@enron.com",
                  "ccalger@enron.com",
                  "tim_despain.enronxgate.enron@enron.net",
                  "tim.despain@enron.com",
                  "kevin_hannon@enron.com",
                  "kevin'.'hannon@enron.com",
                  "kevin_hannon@enron.net",
                  "kevin.hannon@enron.com",
                  "mkoenig@enron.com",
                  "mark.koenig@enron.com",
                  "m..forney@enron.com",
                  "ken'.'rice@enron.com",
                  "ken.rice@enron.com",
                  "ken_rice@enron.com",
                  "ken_rice@enron.net",
                  "paula.rieker@enron.com",
                  "prieker@enron.com",
                  "andrew.fastow@enron.com",
                  "lfastow@pdq.net",
                  "andrew.s.fastow@enron.com",
                  "lfastow@pop.pdq.net",
                  "andy.fastow@enron.com",
                  "david.w.delainey@enron.com",
                  "delainey.dave@enron.com",
                  "'delainey@enron.com",
                  "david.delainey@enron.com",
                  "'david.delainey'@enron.com",
                  "dave.delainey@enron.com",
                  "delainey'.'david@enron.com",
                  "ben.glisan@enron.com",
                  "bglisan@enron.com",
                  "ben_f_glisan@enron.com",
                  "ben'.'glisan@enron.com",
                  "jeff.richter@enron.com",
                  "jrichter@nwlink.com",
                  "lawrencelawyer@aol.com",
                  "lawyer'.'larry@enron.com",
                  "larry_lawyer@enron.com",
                  "llawyer@enron.com",
                  "larry.lawyer@enron.com",
                  "lawrence.lawyer@enron.com",
                  "tbelden@enron.com",
                  "tim.belden@enron.com",
                  "tim_belden@pgn.com",
                  "tbelden@ect.enron.com",
                  "michael.kopper@enron.com",
                  "dave.duncan@enron.com",
                  "dave.duncan@cipco.org",
                  "duncan.dave@enron.com",
                  "ray.bowen@enron.com",
                  "raymond.bowen@enron.com",
                  "'bowen@enron.com",
                  "wes.colwell@enron.com",
                  "dan.boyle@enron.com",
                  "cloehr@enron.com",
                  "chris.loehr@enron.com"
                  ]
    return email_list


if __name__ == "__main__":
    sys.exit(main(sys.argv))
