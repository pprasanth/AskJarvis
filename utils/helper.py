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