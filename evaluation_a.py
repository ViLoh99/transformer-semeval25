# Evaluation for subtask A

from scipy import stats

# check if the picture at rank 1 is correct
def first_accuracy(array1,array2):
    if array1[0] == array2[0]:
        return 1
    else:
        return 0

# calculate Spearman's rank correlation
def spearman(array1,array2):
    return stats.spearmanr(array1,array2).statistic

# give results for both as array
def evaluation_single(guesses,expected):
# guesses & expected are arrays containing the picture file names
    return[first_accuracy(guesses,expected),
           spearman(guesses,expected)]

def evaluation_multiple(guesses,expected):
# guesses & expected are arrays containing arrays for the individual training examples

    first_accuracy_results = []
    spearman_results = []

    for i in range(len(guesses)):
        results_i = evaluation_single(guesses[i], expected[i])
        first_accuracy_results.append(results_i[0])
        spearman_results.append(results_i[1])
    
    return [first_accuracy_results,spearman_results]

# made separate for development process
# might be better to include this into evaluation method above
def evaluate(guesses,expected):
    results = evaluation_multiple(guesses,expected)
    first_acc_average = sum(results[0]) / len(results[0])
    spearman_average = sum(results[1]) / len(results[1])
    return [first_acc_average,spearman_average]