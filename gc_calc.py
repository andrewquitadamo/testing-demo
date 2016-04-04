def gc(sequence):
    gc_count = 0
    total_count = 0
    for nuc in sequence:
        if nuc == 'G':
            gc_count += 1
        if nuc == 'C':
            gc_count += 1
        total_count += 1

    return (float(gc_count) / total_count)
