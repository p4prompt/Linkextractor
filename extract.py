import requests
from bs4 import BeautifulSoup

base_url = 'https://nexdrive.fun/genxfm7847763'
start_number = 75003
end_number = 75100

with open('link_status2.txt', 'w') as f:
    for i in range(start_number, end_number + 1):
        link = base_url + str(i)
        try:
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                title_tag = soup.find('title')
                if title_tag is not None:
                    title = title_tag.string.strip()
                    print(f"{link} is OK, Title: {title}")
                    f.write(f"{link} is OK, Title: {title}\n")
                else:
                    print(f"{link} is OK but does not have a title tag")
            else:
                print(f"{link} returned status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {link}: {e}")
