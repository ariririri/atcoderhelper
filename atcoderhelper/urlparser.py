from bs4 import  BeautifulSoup
import certifi
import urllib3 
from pathlib import Path

class UrlParser():
    def __init__(self,contest):
        """
        contest = abc106
        """
        self.http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where()
        )
        self.contest = contest
        test_url =  f"https://{self.contest}.contest.atcoder.jp/tasks/{self.contest}_c"
        soup = self.get_soup(test_url)
        data = soup.find_all("pre")
        self.data = data
        length = len(soup.find_all("pre") )
        #for i in range(1,length // 2,2):
        #    with open("test_atcoder-{}-test.txt".format( i // 2 + 1),"w")  as f:
        #        f.write(data[i].text)
    
    def write_data(self, dir, data, problem):
        if type(dir) != "pathlib.PosixPath":
            dir = Path(dir)
        inputs = [d for i,d in enumerate(data) if i % 2 == 0]
        outputs = [d for i,d in enumerate(data) if i % 2 == 1]
        for i, (inp,out) in enumerate(zip(inputs, outputs)):
            with open(dir / f"test_{problem}_{i}_input.txt", "w") as f:
                f.write(inp)
            with open(dir / f"test_{problem}_{i}_output.txt", 'w') as f:
                f.write(out)

    
    def get_inputs(self, url):
        soup = self.get_soup(url)
        _data = soup.find_all("pre")
        # なぜか二回数えられるので,一度目だけにする
        length = len(soup.find_all("pre") )
        data = [d.text for i,d in enumerate(_data) if i > 0 and i <= length // 2]
        return data

    def get_problems(self):
        task_url =  f"https://atcoder.jp/contests/{self.contest}/tasks"
        soup = self.get_soup(task_url)
        href_urls = soup.find(id="main-container").div.tbody.find_all("a")
        problem_urls = ["https://atcoder.jp" + url["href"] for i, url in enumerate(href_urls) if i % 2 == 0]
        self.problem_urls = problem_urls
        return problem_urls
    
    def get_soup(self, url):
        print(url)
        request = self.http.request('GET', url)
        return BeautifulSoup(request.data, 'html.parser')


