# retrieve zuluru id from tuc website
# can't do it anymore,m need authorization

import requests
import re
import pprint as pp

def test():
    tuc_base_url = "https://www.tuc.org/zuluru/people/view?person="
    url = tuc_base_url + str(41166)
    r = requests.get(url)
    html_content = r.content.decode('utf-8')

    print(html_content)

def main():

    # id -> player name
    player_dict = {}

    # example url: https://www.tuc.org/zuluru/people/view?person=41184

    tuc_base_url = "https://www.tuc.org/zuluru/people/view?person="

    for i in range(41100, 41200):
        tuc_player_url = tuc_base_url + str(i)
        # set header request?
        
        r = requests.get(tuc_player_url)
        html_content = r.content.decode('utf-8')

        find_regex = "<title>People &raquo; (\w+ \w+) &raquo; View"
        found = re.search(find_regex, html_content)
        
        if found:
            print(found.group(1))
            player_name = found.group(1)
            player_dict[i] = player_name
        else:
            print("player id: " + str(i) + " not found")
        
    
    
    # pp.pprint(player_dict)

if __name__ == '__main__':
    test()