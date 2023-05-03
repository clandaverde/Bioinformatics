from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# * one dict/view *

# sends a http request to view index.html view
def index(request):
    return render(request, 'index.html')

# helper function for sendResult logic
def fill_array(request, j, i, genotype1, genotype2):
    offspring = genotype1[j] + genotype2[i]
    # if the first character is lowercase ensure that the
    # dominant trait comes first by reversing the genotype, wont work for dihybrid crosses
    if offspring[0].isupper() == False:
        offspring = offspring[::-1]
    #print("im the offspring: ", offspring)
    return offspring

def sendResult(request):
    context = {}
    context['name'] = 'square'
    genotype1 = str(request.POST.get('p1geno', False))
    genotype2 = str(request.POST.get('p2geno', False))
    l_offsprings = []

    for i in range(len(genotype1)):
        for j in range(len(genotype2)):
            # pass in j first since it indexes to 1 quicker
            p_offspring = fill_array(request, j, i, genotype1, genotype2)
            l_offsprings.append(p_offspring)
    context['offsprings'] = l_offsprings

    return render(request, 'hello.html', context)
