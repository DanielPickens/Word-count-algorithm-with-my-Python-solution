String analyzing = start;
int curCount = 1;
while (true) {
    if (analyzing.equals(end)) {
        return curCount;
    }
    for (String item : dict.toArray(new String[dict.size()])) {
        if (isSingleCharDiff(analyzing, item)) {
            dict.remove(item);
            lengthCount.add(curCount + 1);
            wordSearch.add(item);
        }
    }
    if (wordSearch.isEmpty()) {
        break;
    }
    analyzing = wordSearch.pop();
    curCount = lengthCount.pop();
}
