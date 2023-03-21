from selenium import webdriver
from flask import Flask, jsonify
from flask_restful import Api, Resource
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920,1080")
path = 'chromedriver.exe'
driver = webdriver.Chrome(path,chrome_options=chrome_options)
driver.maximize_window()
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
api = Api(app)

class getTrendingTopic(Resource):
    def get(self):
        url = "https://trends.google.com/trends/trendingsearches/daily?geo=SG"
        trendingTopics = []
        driver.maximize_window()
        driver.get(url)
        ListDiv = driver.find_element_by_class_name("feed-list-wrapper")
        searchesDiv = ListDiv.find_elements_by_class_name("search-count-title")
        detailsDiv = ListDiv.find_elements_by_class_name("details")
        sourceTimeDiv = ListDiv.find_elements_by_class_name('source-and-time')
        for details, searches, time in zip(detailsDiv, searchesDiv, sourceTimeDiv):
            topic = details.find_element_by_class_name("details-top").find_element_by_xpath("div/span/a").text
            newsLink = details.find_element_by_class_name("details-bottom").find_element_by_xpath("div/div/a").get_attribute('href')
            searchCount = searches.text
            time = time.text[-7:-4]
            trendingTopics.append([topic, time, newsLink, searchCount])

        return jsonify(trendingTopics[:7])

api.add_resource(getTrendingTopic, '/')
# @app.route("/")
# def get_top_trending_topics():
#     url = "https://trends.google.com/trends/trendingsearches/daily?geo=SG"
#     trendingTopics = {}
#     driver.maximize_window()
#     driver.get(url)
#     ListDiv = driver.find_element_by_class_name("feed-list-wrapper")
#     searchesDiv = ListDiv.find_elements_by_class_name("search-count-title")
#     detailsDiv = ListDiv.find_elements_by_class_name("details")
#     sourceTimeDiv = ListDiv.find_elements_by_class_name('source-and-time')
#     for i in range(7):
#         topic = detailsDiv[i].find_element_by_class_name("details-top").find_element_by_xpath("div/span/a").text
#         newsLink = detailsDiv[i].find_element_by_class_name("details-bottom").find_element_by_xpath("div/div/a").get_attribute('href')
#         searchCount = searchesDiv[i].text
#         time = sourceTimeDiv[i].text[-7:-4]
#         trendingTopics[topic] = (time, newsLink, searchCount)

#     return jsonify({'trending':trendingTopics})


if __name__ == '__main__':
    app.run(debug=True)