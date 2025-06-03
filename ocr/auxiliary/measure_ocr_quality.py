import Levenshtein as lev

def measure_ocr_quality(ocr_output, ground_truth):
    """
    Calculates precision, recall, and F1-score
    using the Levenshtein distance to align text from OCR with the ground truth data.

    :param ocr_output: A string containing the raw OCR results.
    :param ground_truth: A string containing the verified ground truth text.
    """

    matching_parts = lev.matching_blocks(lev.editops(ocr_output, ground_truth), ocr_output, ground_truth)
    true_pos = len(''.join([ocr_output[x[0]:x[0]+x[2]] for x in matching_parts]))

    precision = true_pos / len(ground_truth)
    recall = true_pos / len(ocr_output)
    f_score = 2 * ((precision * recall) / (precision + recall))

    return precision, recall, f_score