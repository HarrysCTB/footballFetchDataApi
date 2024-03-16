from django.shortcuts import render
from .utils import get_data_from_api

def myScore(score):
    tmp = ""
    tmp = str(score['home'])
    tmp = tmp + "   -   "
    tmp = tmp + str(score['away'])
    for key in score:
        if (key == 'fullTime'):
            for goal in key:
                if (goal == "NONE"):
                    myList.append(key["Match à venir"])
                myList.append(key[goal])
    return tmp


def index(request):
    data = get_data_from_api()
    homeTeamList = []
    if data:
        valeur_api = data['matches']
    else:
        valeur_api = None
    for name in valeur_api:
        for key, value in name.items():
            if (key == 'homeTeam'):
                buff =  value['name']
            if (key == 'awayTeam'):
                tmp = value['name']
            if (key == 'score'):
                buff = buff + "<br>" + tmp
                buff = buff + '<span class="rightText">' + (myScore(value['fullTime'])) + "</span>"
                tmp = ""
                homeTeamList.append(buff)
    context  = {
        'homeTeamList': homeTeamList,
    }
    print(valeur_api)
    return render(request, 'football_app/index.html', context)

