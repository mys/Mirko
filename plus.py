import datetime
import json
import jsonpickle
import sys
import time
import wykop
from pprint import pprint

api = wykop.WykopAPI('aNd401dAPp', '3lWf1lCxD6')
result = api.authenticate(login='satoshi', password='')

#var x = document.getElementsByClassName('button mikro ajax'); 
#for (var i = 0, l = x.length; i < l; i++) {
#if (!x[i].href.includes('comment')) {
##x[i].click();
#console.log(x[i].href); 
#}
#}

result = api.vote_entry('150587')