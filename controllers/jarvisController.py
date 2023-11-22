from flask import render_template, redirect, request, url_for
from chatterbot.trainers import ListTrainer

from app import ask_jarvis

from utils.helper import paginate

from models.jarvis import JarvisModel

class JavisController():
    def list():
        currentPageNo = int(request.args.get('pageNo') if request.args.get('pageNo') is not None else 1)
        query = request.args.get('q') if request.args.get('q') is not None else ""
        count, lists = JarvisModel.listAll(query, currentPageNo)
        page_numnbers, lastPageNo=paginate(count, 10, currentPageNo)
        return render_template('jarvis/list.html', lists=lists, currentPageNo=currentPageNo, page_numnbers=page_numnbers, lastPageNo=lastPageNo, query=query)
    
    def train_jarvis():
        tags = JarvisModel.fetch_tags()
        bot_responses = JarvisModel.fetch_response_list()
        return render_template('jarvis/train.html', tags=tags, bot_responses=bot_responses)
    
    def save_jarvis():
       if request.method == 'POST' and 'text' in request.form and 'in_response_to' in request.form:
            form = request.form
            isSaved = JarvisModel.create_new_training(
                form['text'],
                form['search_text'],
                form['conversation'],
                form['in_response_to'],
                form['search_in_response_to'],
                form['persona'],
                form.getlist('tags'),
            )
            if isSaved:
                success_message = "Trained new data"
                return redirect(url_for('admin_blueprint.list', success_message=success_message))
            else:
                error_message = "Error in training"
                return redirect(url_for('admin_blueprint.list', error_message=error_message))
       else:
            error_message = "Invalid submission"
            return redirect(url_for('admin_blueprint.list', error_message=error_message))
    
    def javis_tags():
        currentPageNo = int(request.args.get('pageNo') if request.args.get('pageNo') is not None else 1)
        query = request.args.get('q') if request.args.get('q') is not None else ""
        count, lists = JarvisModel.listAllTags(query, currentPageNo)
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
          JarvisModel.create_new_tag(request.form['tag'])
          success_message = "Tag created"
          return redirect(url_for('admin_blueprint.javis_tags', success_message=success_message))
        else:
          error_message = "Invalid submission"
          return redirect(url_for('admin_blueprint.javis_tags', error_message=error_message))
        
    def train_conversation():
        return render_template('jarvis/train_converstaion.html')
    
    def load_more_chat():
        input_var = request.args.get('inc')
        return render_template('jarvis/load_more_chat.html', input_var=input_var)
    
    def save_jarvis_conversation():
        trainer = ListTrainer(ask_jarvis)
        training_data = []
        for index, value in enumerate(request.form):
            training_data.append(request.form[value])
        
        trainer.train(training_data)
        success_message = "Trained conversation"
        return redirect(url_for('admin_blueprint.list', success_message=success_message))