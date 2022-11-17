"""
Write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.
For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays.
If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function,
we don't know what is after and before and therefore, we don't know if it is a peak or not).
"""


def pick_peaks(arr):
    pos, peaks = [], []
    output_dict = {"pos": [], "peaks": []}

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            pos, peaks = [i], [arr[i]]

        elif arr[i] < arr[i-1]:
            output_dict["pos"] += pos
            output_dict["peaks"] += peaks
            pos, peaks = [], []

    return output_dict
