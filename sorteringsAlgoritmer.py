import random, copy

def bubbleSort (items):
    n = len(items)
    swapped = False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if items[j]> items[j+1]:
                swapped = True
                items[j], items[j+1] = items[i+1], items[i]

            if not swapped:
                break
    return items



if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = bubbleSort(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('blandet: ', lb)
    print('sorteret:', ls)
