import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from urllib.parse import urljoin

class TargetAnalyzer:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.keywords = ['コーチ', 'コンサル', 'スクール', '講座', 'セミナー', '養成', '起業']

    def analyze_url(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'html.parser')
            
            html_content = response.text
            
            # Check for Meta Pixel
            has_pixel = bool(re.search(r'fbevents\.js|fbq\(', html_content))
            
            # Check for LINE
            line_links = soup.find_all('a', href=re.compile(r'line\.me|liff\.line\.me'))
            has_line = len(line_links) > 0
            
            # Check Keywords
            text_content = soup.get_text()
            matched_keywords = [kw for kw in self.keywords if kw in text_content]
            is_target_industry = len(matched_keywords) > 0
            
            # Scoring
            score = 0
            strategy = ""
            
            if is_target_industry:
                if has_pixel:
                    if not has_line:
                        score = 95
                        strategy = "【激アツ】広告費を垂れ流しています。LINE導入だけでCPAが劇的に下がりますと提案。"
                    else:
                        score = 70
                        strategy = "【要検討】広告もLINEもやっています。ステップ配信やAI化による「自動化・工数削減」を提案。"
                else:
                    if has_line:
                        score = 50
                        strategy = "【潜在】広告は打っていません。オーガニック集客の限界を訴求し、広告運用×LINEを提案。"
                    else:
                        score = 30
                        strategy = "【育成】まだWeb集客の基礎ができていません。"
            else:
                score = 0
                strategy = "対象外"

            return {
                'url': url,
                'title': soup.title.string.strip() if soup.title else 'No Title',
                'has_pixel': has_pixel,
                'has_line': has_line,
                'keywords': ','.join(matched_keywords),
                'score': score,
                'strategy': strategy
            }
            
        except Exception as e:
            return {
                'url': url,
                'title': 'Error',
                'has_pixel': False,
                'has_line': False,
                'keywords': '',
                'score': 0,
                'strategy': f"Connection Error: {str(e)}"
            }

    def process_list(self, url_list):
        results = []
        for url in url_list:
            print(f"Analyzing: {url}...")
            data = self.analyze_url(url)
            results.append(data)
        
        df = pd.DataFrame(results)
        df = df.sort_values('score', ascending=False)
        return df

if __name__ == "__main__":
    # Test with some example URLs (Note: Real URLs would be better, but we use placeholders or safe generic ones for now)
    # In a real scenario, we would feed a list of search results here.
    test_urls = [
        "https://example.com", 
        "https://www.udemy.com/",
        # Add more real-ish targets if possible, or leave blank for user input
    ]
    
    analyzer = TargetAnalyzer()
    df = analyzer.process_list(test_urls)
    print(df)
    df.to_csv('research_tool/leads.csv', index=False)
