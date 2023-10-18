from flask import render_template, session, request, url_for
from models.jarvis import listAll

def paginate(total_items, page_size, current_page):
  total_pages = total_items // page_size + 1
  max_buttons = 6

  # Calculate the start and end page numbers to display.
  start_page = max(1, current_page - max_buttons // 2)
  end_page = min(total_pages, current_page + max_buttons // 2)

  # Create a list of page numbers to display.
  page_numbers = []
  for page_number in range(start_page, end_page + 1):
    page_numbers.append(page_number)

  return page_numbers, total_pages

class JavisController():
    def list():
        currentPageNo = int(request.args.get('pageNo') if request.args.get('pageNo') is not None else 1)
        query = request.args.get('q') if request.args.get('q') is not None else ""
        print(currentPageNo)
        count, lists = listAll(query, currentPageNo)
        page_numnbers, lastPageNo=paginate(count, 10, currentPageNo)
        print(page_numnbers)
        return render_template('jarvis/list.html', lists=lists, currentPageNo=currentPageNo, page_numnbers=page_numnbers, lastPageNo=lastPageNo, query=query)
    
    def train_jarvis():
        return render_template('jarvis/train.html')