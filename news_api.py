import requests
from datetime import datetime

def fetch_news():
    url='https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=5481450d0b5d4684a37c20bca6485dd2'

    response=requests.get(url)
    data=response.json()

    if data['status']=='ok' and 'articles' in data:
        return data['articles']
    else:
        raise Exception('Failed to get news ')

def format_article(article):
    news_title = article.get('title', 'No title available')
    news_description = article.get('description', 'No description available')
    news_url = article.get('url', 'No URL available')
    news_author = article.get('author', 'Unknown')
    news_urlImage = article.get('urlToImage', 'No image available')
    news_upload_time = article.get('publishedAt', 'No time available')

    if news_upload_time != 'No time available':
        dt = datetime.strptime(news_upload_time, "%Y-%m-%dT%H:%M:%SZ")
        formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")
    else:
        formatted_time = 'No time available'
    
    return {
        'title': news_title,
        'description': news_description,
        'url': news_url,
        'author': news_author,
        'image_url': news_urlImage,
        'upload_time': formatted_time
    }

def display_article(article, article_number, total_articles):
    print(f"\n\n--Article {article_number + 1} of {total_articles}-:\n")
    print(f"\t\t\t\t\t***** Title: {article['title']} *****")
    print(f"\n -> Description: {article['description']}")
    print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t-->Author: {article['author']}")
    print(f"  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t-:Upload Time: {article['upload_time']}")
    print(f"\n<- Read Full Article Here: {article['url']} ->")
    # print(f"\n <<- Image URL: {article['image_url']} ->>\n")
    
def main():
    try:
        articles = fetch_news()
        total_articles = len(articles)
        current_article_index = 0
        while True:
            article = format_article(articles[current_article_index])
            display_article(article, current_article_index, total_articles)

            user_input = input("\n\nPress 'n' for next article, 'p' for previous article, or 'q' to quit: ").lower()

            if user_input == 'n':
                if current_article_index < total_articles - 1:
                    current_article_index += 1
                else:
                    print("You are already at the last article.")
            elif user_input == 'p':
                if current_article_index > 0:
                    current_article_index -= 1
                else:
                    print("You are already at the first article.")
            elif user_input == 'q':
                break
            else:
                print("\n\nInvalid input. Please press 'n' for next, 'p' for previous, or 'q' to quit.")
        
    except Exception as e:
        print(str(e))

if __name__=='__main__':
    main()