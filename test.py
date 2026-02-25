

# ### Novel bin

# import cloudscraper
# from bs4 import BeautifulSoup
# from docx import Document
# import time
# from urllib.parse import urljoin
# import re

# doc = Document()
# scraper = cloudscraper.create_scraper(delay=5)

# url = input("Enter the URL of the first chapter: ").strip()
# # base_url = 'https://novelbin.com/' # Not strictly needed with urljoin

# title_fixed = False
# filename = "novel.docx" 
# count = 0 

# while url:
#     print(f"Scraping: {url}")
#     response = scraper.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         count += 1 
        
#         # 1. Novel Title (Using NovelBin's breadcrumb or title class)
#         if not title_fixed:
#             title_tag = soup.find('a', class_='novel-title') or soup.select_one('h2.novel-title a')
#             if title_tag:
#                 novel_title = title_tag.text.strip()
#                 clean_title = re.sub(r'[\\/*?:"<>|]', " ", novel_title)
#                 filename = f"{' '.join(clean_title.split())}.docx"
#                 title_fixed = True

#         # 2. Chapter Title (Usually h2 or the chr-title class)
#         chapter_title = soup.find('span', class_='chr-text')
#         if chapter_title:
#             doc.add_heading(chapter_title.get_text(strip=True), level=1)

#         # 3. Chapter Content (NovelBin uses #chr-content)
#         content = soup.find('div', id='chr-content')
#         if content:
#             # We want just the paragraphs, excluding ads/scripts
#             for p in content.find_all('p', recursive=False):
#                 doc.add_paragraph(p.get_text())

#         # 4. Next Button (NovelBin uses id='next_chap')
#         next_page = soup.find('a', id='next_chap')
#         if next_page and 'href' in next_page.attrs and next_page['href'] != "#":
#             url = urljoin(url, next_page['href'])
            
#             if count % 10 == 0:
#                 doc.save(filename)
#                 print(f"Checkpoint: Saved {count} chapters...")
            
#             time.sleep(1)
#         else:
#             print("No more chapters found.")
#             url = None  

#     elif response.status_code == 403:
#         print("FAILED: Cloudflare 403. Try a VPN or Hotspot.")
#         break
#     else:
#         print(f"Failed: Status {response.status_code}")
#         break

# doc.save(filename)
# print(f"Final document saved as '{filename}'.")