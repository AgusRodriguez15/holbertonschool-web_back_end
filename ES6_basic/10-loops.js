export default function appendToEachArrayValue(array, appendString) {
    let index = 0;
    for (let idx of array) {
      array[idx] = appendString + value;
      index++;
    }
  
    return array;
  }