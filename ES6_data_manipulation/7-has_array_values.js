function hasValueFromArray(set, array) {
    const check = array.every((item) => set.has(item));
    return check;
}

export default hasValueFromArray;
