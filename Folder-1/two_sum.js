function findIndicesSum(array, targetValue) {
    for (let i = 0; i < array.length - 1; i++) {
        for (let j = i + 1; j < array.length; j++) {
            if (targetValue === array[i] + array[j]) {
                return [i, j];
            }
        }
    }
    return [];
}

array1 = [1, 2, 3, 4, 5]
target = 9

console.log(findIndicesSum(array1, target))