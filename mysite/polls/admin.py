from django.contrib import admin

from .models import Question, Choice


# displaying Question and Choice models on the admin index page
# admin.site.register(Question)
# admin.site.register(Choice)




# With changing the ChoiceInline declaration,
# it makes the display on choice web page different
# for example, if I use a TabularInline, the objects are displayed
# more compact, compare to using StackedInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3




class QuestionAdmin(admin.ModelAdmin):
    #fieldsets = [
        #(None,               {'fields': ['question_text']}),
        #('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    #inlines = [ChoiceInline]
	
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']
	
	


admin.site.register(Question, QuestionAdmin)




# these code change the display for the admin change question web page
# the question text field is on top and publication date filed is bottom
    #fieldsets = [
        #(None,               {'fields': ['question_text']}),
        #('Date information', {'fields': ['pub_date']}),
    #]

#admin.site.register(Question, QuestionAdmin)









    #fields = ['pub_date', 'question_text']
#admin.site.register(Question, QuestionAdmin)




    #fieldsets = [
        #(None,               {'fields': ['question_text']}),
        #('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
	    #list_display = ('question_text', 'pub_date', 'was_published_recently')
		
		#list_filter = ['pub_date'] # it adds a filter slidebar to let people filter their publication date
        #inlines = [ChoiceInline]
		#search_fields = ['question_text']
	
	
    # this will make the publication date field come first than the question field
    # fields = ['pub_date', 'question_text']
	



