from django.shortcuts import render, render_to_response, redirect
from haystack.query import SearchQuerySet
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from django.http import HttpResponse


@csrf_exempt
def SearchQueryView(request):
    query_text = request.GET.get('q', '')
    if query_text == '':
        return redirect('home')
    else:
        courses = SearchQuerySet().filter(
            content_auto=query_text)
        return render_to_response('search/search.html', {'courses': courses})


def SearchQueryAutocomplete(request):
    sqs = SearchQuerySet().autocomplete(
        content_auto=request.GET.get('q', ''))
    suggestions = [result.title for result in sqs]
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')
