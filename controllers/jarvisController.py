from flask import render_template, redirect, request, url_for
from models.jarvis import listAll, create_new_tag, listAllTags

from utils.helper import paginate

class JavisController():
    def list():
        currentPageNo = int(request.args.get('pageNo') if request.args.get('pageNo') is not None else 1)
        query = request.args.get('q') if request.args.get('q') is not None else ""
        count, lists = listAll(query, currentPageNo)
        page_numnbers, lastPageNo=paginate(count, 10, currentPageNo)
        return render_template('jarvis/list.html', lists=lists, currentPageNo=currentPageNo, page_numnbers=page_numnbers, lastPageNo=lastPageNo, query=query)
    
    def train_jarvis():
        return render_template('jarvis/train.html')
    
    def javis_tags():
        currentPageNo = int(request.args.get('pageNo') if request.args.get('pageNo') is not None else 1)
        query = request.args.get('q') if request.args.get('q') is not None else ""
        count, lists = listAllTags(query, currentPageNo)
        page_numnbers, lastPageNo=paginate(count, 10, currentPageNo)
        success_message = request.args.get('success_message') if request.args.get('success_message') is not None else ""
        error_message = request.args.get('error_message') if request.args.get('error_message') is not None else ""
  
        return render_template(
           'jarvis/tags.html',
           success_message=success_message,
           error_message=error_message,
           lists=lists,
           currentPageNo=currentPageNo,
           page_numnbers=page_numnbers,
           lastPageNo=lastPageNo,
           query=query,
        )
    
    def save_tags():
        if request.method == 'POST' and 'tag' in request.form:
          create_new_tag(request.form['tag'])
          success_message = "Tag created"
          return redirect(url_for('admin_blueprint.javis_tags', success_message=success_message))
        else:
          error_message = "Invalid submission"
          return redirect(url_for('admin_blueprint.javis_tags', error_message=error_message))