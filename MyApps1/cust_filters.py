from django import template;
register=template.Library()
def first_five_upper(value):
  #This is my own filter
          result=value[:5].upper();
          return result;
          register.filter('f5upper', first_five_upper);
