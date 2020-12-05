## Search Engine Optimization System

The purpose of building this application is to make it easier for people who need to optimize their SEO in order to ensure a good organic traffic to their websites.

This system will crawl Google Trends, Twitter and other websites for trending Keywords.
Then we analyze those words with some sentiment analysis algorithms (TextBlob). We also used Sklearn-cluster to apply the KMeans clustering algorithm on these words, in order to group similar ones, which will be very useful for our application.

the technologies used during the development of our application:

- Flask,
- GraphQL,
- Angular 8,
- HighCharts,
- MongoDB,
- Pandas,
- BeautifulSoup,
- Bootstrap,
- Vagrant.

Some screenshots of the app:

<p align="center">
  <p>Landing Page</p>
  <img src="https://user-images.githubusercontent.com/48560744/101241570-920bc900-36f7-11eb-8150-7b900b56eaea.png" width="750" title="Landing Page">
</p>

<p align="center">
  <p>Trendy Keywords on Google Trends</p>
  <img src="https://user-images.githubusercontent.com/48560744/101241573-946e2300-36f7-11eb-80bf-8c6c21749185.png" width="750">
</p>


<p align="center">
  <p>Intrest by Time in some Keywords </p>
  <img src="https://user-images.githubusercontent.com/48560744/101241574-9637e680-36f7-11eb-860a-5e8911e7f38d.png" width="750">
</p>

<p align="center">
  <p>TOP Tweets And Positivity of the Day </p>
  <img src="https://user-images.githubusercontent.com/48560744/101241575-989a4080-36f7-11eb-84ef-ad744d6d3824.png" width="750">
</p>

<p align="center">
  <p>Looking for a specific keyword (example: Trump), we get similar words according to the KMeans algorithm (the bar at the top). At the bottom, we have a table that contains a list of suggested additional keywords with a score (Max 100), and a type (Top or Rising).</p>
  <img src="https://user-images.githubusercontent.com/48560744/101241576-9afc9a80-36f7-11eb-82e9-ed15c26cf16d.png" width="750">
</p>

<p align="center">
  <p>World map with searched word interest in relation to Countries.</p>
  <img src="https://user-images.githubusercontent.com/48560744/101241577-9c2dc780-36f7-11eb-95e0-d8c2580aaf5b.png" width="750">
</p>




